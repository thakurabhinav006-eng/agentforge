from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are an AI health and fitness planner. You create personalized workout plans,
meal plans, track fitness goals, and provide nutrition advice. Ask about fitness level,
goals, dietary restrictions, available equipment, and schedule. Disclaim you are not
a certified trainer or dietitian. Create structured weekly plans."""


class HealthFitnessAgent(BaseAgent):
    info = AgentInfo(
        id="health-fitness",
        name="Health & Fitness",
        description="Personalized workout plans, meal plans, and nutrition guidance",
        category="starter",
        icon="heart-pulse",
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
