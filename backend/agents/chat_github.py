from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_groq

SYSTEM = """You are a GitHub repository analysis assistant. You help users understand
codebases, explain code architecture, review PRs, analyze issues, suggest improvements,
and generate documentation. When given repo info or code, provide clear technical analysis."""


class ChatGitHubAgent(BaseAgent):
    info = AgentInfo(
        id="chat-github",
        name="Chat with GitHub",
        description="Analyze repos, understand codebases, review code, and generate docs",
        category="rag",
        icon="github",
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
