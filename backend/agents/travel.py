from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an expert AI travel planner. You create detailed itineraries,
suggest destinations, find activities, estimate budgets, and provide local tips.
Ask about travel dates, budget, preferences, and group size.
Format itineraries with day-by-day breakdowns."""


class TravelAgent(BaseAgent):
    info = AgentInfo(
        id="travel",
        name="Travel Planner",
        description="Plan trips with detailed itineraries, budgets, and local recommendations",
        category="starter",
        icon="plane",
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
