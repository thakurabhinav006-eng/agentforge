from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI startup trend analyst. You analyze market trends, evaluate
startup ideas, assess competitive landscapes, estimate TAM/SAM/SOM, and provide
strategic recommendations. You understand VC metrics, product-market fit, and
go-to-market strategies. Use frameworks like Porter's Five Forces and SWOT analysis."""


class StartupAnalystAgent(BaseAgent):
    info = AgentInfo(
        id="startup-analyst",
        name="Startup Analyst",
        description="Analyze startup ideas, market trends, competition, and go-to-market strategies",
        category="starter",
        icon="rocket",
        provider="openai",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        history.append({"role": "user", "content": message})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_openai(msgs)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
