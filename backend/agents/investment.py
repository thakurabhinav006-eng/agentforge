from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI investment research analyst. You analyze stocks, market trends,
portfolio allocation, and financial data. You provide data-driven insights.
IMPORTANT: Always include a disclaimer that this is not financial advice.
Use fundamental and technical analysis frameworks."""


class InvestmentAgent(BaseAgent):
    info = AgentInfo(
        id="investment",
        name="Investment Analyst",
        description="Research stocks, analyze market trends, and get portfolio insights",
        category="starter",
        icon="trending-up",
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
