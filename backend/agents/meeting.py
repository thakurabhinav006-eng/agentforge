from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI meeting assistant. You help with meeting preparation,
create agendas, take meeting notes, generate action items, write follow-up emails,
and summarize discussions. Format output clearly with sections for attendees,
agenda items, decisions made, and action items with owners and deadlines."""


class MeetingAgent(BaseAgent):
    info = AgentInfo(
        id="meeting",
        name="Meeting Assistant",
        description="Create agendas, take notes, generate action items, and write follow-ups",
        category="starter",
        icon="calendar",
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
