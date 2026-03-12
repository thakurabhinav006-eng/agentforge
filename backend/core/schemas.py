from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str
    agent_id: str
    session_id: Optional[str] = None
    context: Optional[dict] = None


class ChatResponse(BaseModel):
    reply: str
    agent_id: str
    session_id: str
    metadata: Optional[dict] = None


class AgentInfo(BaseModel):
    id: str
    name: str
    description: str
    category: str
    icon: str
    provider: str
    input_type: str = "text"
    supports_file: bool = False
