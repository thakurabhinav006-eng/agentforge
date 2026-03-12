from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an advanced reasoning agent. You solve complex problems using
chain-of-thought reasoning. Break down problems step by step, consider multiple
angles, evaluate evidence, identify assumptions, and reach well-supported conclusions.
Show your reasoning process transparently. Handle logic puzzles, math, code debugging,
and strategic decisions."""


class ReasoningAgent(BaseAgent):
    info = AgentInfo(
        id="reasoning",
        name="Reasoning Engine",
        description="Solve complex problems with step-by-step chain-of-thought reasoning",
        category="starter",
        icon="brain",
        provider="groq",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        history.append({"role": "user", "content": message})
        resp = chat_groq([{"role": "system", "content": SYSTEM}] + history)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
