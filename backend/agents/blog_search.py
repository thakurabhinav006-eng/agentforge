from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI blog search and content research assistant. You help users
find relevant articles, summarize blog posts, extract key insights, compare perspectives
across sources, and create content briefs. Help with SEO analysis and content strategy."""


class BlogSearchAgent(BaseAgent):
    info = AgentInfo(
        id="blog-search",
        name="Blog Search & Research",
        description="Search blogs, summarize articles, extract insights, and create content briefs",
        category="rag",
        icon="search",
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
