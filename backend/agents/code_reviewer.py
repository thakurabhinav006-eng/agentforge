from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_anthropic

SYSTEM = """You are a senior code reviewer. You review code for bugs, security vulnerabilities,
performance issues, code smells, and best practices. Provide specific, actionable feedback
with code examples. Rate severity: critical, major, minor, suggestion.
Support all major languages: Python, JavaScript, TypeScript, Go, Rust, Java, C++."""


class CodeReviewerAgent(BaseAgent):
    info = AgentInfo(
        id="code-reviewer",
        name="Code Reviewer",
        description="Review code for bugs, security issues, performance, and best practices",
        category="multi-agent",
        icon="code",
        provider="anthropic",
        supports_file=True,
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        content = message
        if context and context.get("file_content"):
            content = f"Code to review:\n```\n{context['file_content'][:12000]}\n```\n\n{message}"
        history.append({"role": "user", "content": content})
        resp = chat_anthropic(history, system=SYSTEM)
        reply = resp.content[0].text
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
