from abc import ABC, abstractmethod
from core.schemas import AgentInfo
import uuid


class BaseAgent(ABC):
    info: AgentInfo

    def __init__(self):
        self.sessions: dict[str, list] = {}

    def get_session(self, session_id: str | None) -> tuple[str, list]:
        sid = session_id or str(uuid.uuid4())
        if sid not in self.sessions:
            self.sessions[sid] = []
        return sid, self.sessions[sid]

    @abstractmethod
    async def run(self, message: str, session_id: str | None = None, context: dict | None = None) -> dict:
        pass
