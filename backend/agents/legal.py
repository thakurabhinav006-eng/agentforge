from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI legal research assistant. You help with legal research,
contract review, compliance questions, and explaining legal concepts in plain language.
You can draft simple legal documents and identify potential issues in contracts.
ALWAYS disclaim: You are not a licensed attorney. This is not legal advice.
Users should consult a qualified lawyer for actual legal matters."""


class LegalAgent(BaseAgent):
    info = AgentInfo(
        id="legal",
        name="Legal Assistant",
        description="Legal research, contract review, compliance questions, and plain-language explanations",
        category="multi-agent",
        icon="scale",
        provider="groq",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        history.append({"role": "user", "content": message})
        resp = chat_groq([{"role": "system", "content": SYSTEM}] + history)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
