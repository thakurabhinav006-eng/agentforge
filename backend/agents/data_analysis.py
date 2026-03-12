from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are an AI data analysis expert. You help users analyze datasets,
generate insights, create visualizations descriptions, write SQL queries,
and explain statistical concepts. When given data, provide summary statistics,
identify patterns, and suggest actionable insights.
Output code snippets in Python (pandas, matplotlib) when helpful."""


class DataAnalysisAgent(BaseAgent):
    info = AgentInfo(
        id="data-analysis",
        name="Data Analyst",
        description="Analyze datasets, generate insights, and create visualization suggestions",
        category="starter",
        icon="bar-chart",
        provider="openai",
        supports_file=True,
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        content = message
        if context and context.get("file_content"):
            content = f"Data:\n```\n{context['file_content'][:8000]}\n```\n\nUser query: {message}"
        history.append({"role": "user", "content": content})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_openai(msgs)
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
