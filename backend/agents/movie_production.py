from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI movie production assistant. You help with screenplay writing,
story development, character creation, scene breakdowns, shot lists, casting suggestions,
budget estimation, and production scheduling. Understand film industry terminology
and standard formats like Final Draft screenplay format."""


class MovieProductionAgent(BaseAgent):
    info = AgentInfo(
        id="movie-production",
        name="Movie Production",
        description="Screenplay writing, story development, scene breakdowns, and production planning",
        category="starter",
        icon="clapperboard",
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
