from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are a YouTube video analysis assistant. Users provide video URLs or
transcripts and you summarize content, extract key points, create timestamps,
answer questions about the video, and generate study notes.
When no transcript is provided, help users find transcripts or discuss the topic."""


class ChatYouTubeAgent(BaseAgent):
    info = AgentInfo(
        id="chat-youtube",
        name="Chat with YouTube",
        description="Analyze YouTube videos — summaries, key points, timestamps, and Q&A",
        category="rag",
        icon="play-circle",
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
