from agents.base import BaseAgent
from core.schemas import AgentInfo
from core.llm import chat_openai

SYSTEM = """You are a document analysis AI. Users upload PDF/text content and you
answer questions about it. Provide accurate answers based ONLY on the provided document.
If the answer is not in the document, say so. Quote relevant sections when possible.
Summarize, extract key points, and answer specific questions."""


class ChatPDFAgent(BaseAgent):
    info = AgentInfo(
        id="chat-pdf",
        name="Chat with PDF",
        description="Upload documents and ask questions — get answers based on the content",
        category="rag",
        icon="file-text",
        provider="openai",
        supports_file=True,
        input_type="file",
    )

    async def run(self, message: str, session_id=None, context=None):
        sid, history = self.get_session(session_id)
        content = message
        if context and context.get("file_content"):
            content = f"Document content:\n```\n{context['file_content'][:12000]}\n```\n\nQuestion: {message}"
        history.append({"role": "user", "content": content})
        msgs = [{"role": "system", "content": SYSTEM}] + history
        resp = chat_openai(msgs, model="gpt-4o")
        reply = resp.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return {"reply": reply, "session_id": sid}
