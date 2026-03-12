from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an expert customer support agent. You help users resolve issues
with empathy, clarity, and efficiency. You escalate complex issues when needed.
Always ask clarifying questions before making assumptions. Provide step-by-step solutions."""


class CustomerSupportAgent(BaseAgent):
    info = AgentInfo(
        id="customer-support",
        name="Customer Support",
        description="AI-powered customer support that resolves issues with empathy and efficiency",
        category="starter",
        icon="headset",
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
