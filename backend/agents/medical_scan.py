from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI medical education assistant. You help users understand
medical imaging concepts, explain common findings in X-rays, CT scans, and MRIs.
CRITICAL: Always state you are NOT a doctor and cannot provide medical diagnoses.
Encourage users to consult healthcare professionals for actual medical advice.
You are for educational purposes only."""


class MedicalScanAgent(BaseAgent):
    info = AgentInfo(
        id="medical-scan",
        name="Medical Scan Educator",
        description="Learn about medical imaging, scan types, and common findings (educational only)",
        category="starter",
        icon="scan",
        provider="groq",
        supports_file=True,
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        history.append({"role": "user", "content": message})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_groq(msgs)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
