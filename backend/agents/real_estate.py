from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI real estate advisor. You help with property analysis,
market comparisons, mortgage calculations, investment property evaluation,
neighborhood analysis, and home buying/selling strategies. Provide data-driven
insights with estimated numbers. Disclaim you are not a licensed real estate agent."""


class RealEstateAgent(BaseAgent):
    info = AgentInfo(
        id="real-estate",
        name="Real Estate Advisor",
        description="Property analysis, market comparisons, mortgage calculations, and investment evaluation",
        category="multi-agent",
        icon="building",
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
