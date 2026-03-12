from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from core.schemas import ChatRequest, ChatResponse
from agents import get_agent, list_agents
from typing import Optional

router = APIRouter(prefix="/api/v1", tags=["agents"])


@router.get("/agents")
def get_all_agents():
    return list_agents()


@router.get("/agents/{agent_id}")
def get_agent_info(agent_id: str):
    agent = get_agent(agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")
    return agent.info.model_dump()


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    agent = get_agent(req.agent_id)
    if not agent:
        raise HTTPException(404, f"Agent '{req.agent_id}' not found")
    result = await agent.run(req.message, req.session_id, req.context)
    return ChatResponse(
        reply=result["reply"],
        agent_id=req.agent_id,
        session_id=result["session_id"],
    )


@router.post("/chat/file")
async def chat_with_file(
    message: str = Form(...),
    agent_id: str = Form(...),
    session_id: Optional[str] = Form(None),
    file: UploadFile = File(...),
):
    agent = get_agent(agent_id)
    if not agent:
        raise HTTPException(404, f"Agent '{agent_id}' not found")
    content = (await file.read()).decode("utf-8", errors="ignore")
    context = {"file_content": content, "file_name": file.filename}
    result = await agent.run(message, session_id, context)
    return ChatResponse(
        reply=result["reply"],
        agent_id=agent_id,
        session_id=result["session_id"],
    )
