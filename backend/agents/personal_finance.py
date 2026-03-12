from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are a personal finance advisor AI. You help with budgeting, savings plans,
debt management, tax optimization, and retirement planning. Break down complex financial
concepts simply. Always disclaim you are not a licensed financial advisor.
Create actionable plans with specific numbers when possible."""


class PersonalFinanceAgent(BaseAgent):
    info = AgentInfo(
        id="personal-finance",
        name="Personal Finance",
        description="Budget planning, savings goals, debt management, and financial advice",
        category="starter",
        icon="wallet",
        provider="groq",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        history.append({"role": "user", "content": message})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_groq(msgs)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
