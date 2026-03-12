from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI recruitment assistant. You help with writing job descriptions,
screening resumes, generating interview questions, evaluating candidates, and creating
hiring pipelines. You understand various tech stacks, soft skills assessment, and
diversity-inclusive hiring practices. Output structured evaluations."""


class RecruitmentAgent(BaseAgent):
    info = AgentInfo(
        id="recruitment",
        name="Recruitment Assistant",
        description="Write job posts, screen resumes, generate interview questions, evaluate candidates",
        category="multi-agent",
        icon="users",
        provider="openai",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        content = message
        if context and context.get("file_content"):
            content = f"Resume/Document:\n```\n{context['file_content'][:8000]}\n```\n\n{message}"
        history.append({"role": "user", "content": content})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_openai(msgs)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
