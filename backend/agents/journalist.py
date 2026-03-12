from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI journalist agent. You research topics, fact-check claims,
write news articles, create summaries of events, and conduct interviews.
Follow AP style guidelines. Always cite sources when possible.
Present balanced viewpoints and distinguish facts from opinions."""


class JournalistAgent(BaseAgent):
    info = AgentInfo(
        id="journalist",
        name="AI Journalist",
        description="Research topics, write articles, fact-check, and create news summaries",
        category="starter",
        icon="newspaper",
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
