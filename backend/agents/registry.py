from agents.base import BaseAgent
from agents.customer_support import CustomerSupportAgent
from agents.investment import InvestmentAgent
from agents.travel import TravelAgent
from agents.data_analysis import DataAnalysisAgent
from agents.personal_finance import PersonalFinanceAgent
from agents.journalist import JournalistAgent
from agents.medical_scan import MedicalScanAgent
from agents.meeting import MeetingAgent
from agents.reasoning import ReasoningAgent
from agents.health_fitness import HealthFitnessAgent
from agents.legal import LegalAgent
from agents.recruitment import RecruitmentAgent
from agents.real_estate import RealEstateAgent
from agents.startup_analyst import StartupAnalystAgent
from agents.chat_pdf import ChatPDFAgent
from agents.chat_youtube import ChatYouTubeAgent
from agents.chat_github import ChatGitHubAgent
from agents.blog_search import BlogSearchAgent
from agents.code_reviewer import CodeReviewerAgent
from agents.movie_production import MovieProductionAgent

_AGENTS: list[type[BaseAgent]] = [
    CustomerSupportAgent,
    InvestmentAgent,
    TravelAgent,
    DataAnalysisAgent,
    PersonalFinanceAgent,
    JournalistAgent,
    MedicalScanAgent,
    MeetingAgent,
    ReasoningAgent,
    HealthFitnessAgent,
    LegalAgent,
    RecruitmentAgent,
    RealEstateAgent,
    StartupAnalystAgent,
    ChatPDFAgent,
    ChatYouTubeAgent,
    ChatGitHubAgent,
    BlogSearchAgent,
    CodeReviewerAgent,
    MovieProductionAgent,
]

AGENT_REGISTRY: dict[str, BaseAgent] = {cls.info.id: cls() for cls in _AGENTS}


def get_agent(agent_id: str) -> BaseAgent | None:
    return AGENT_REGISTRY.get(agent_id)


def list_agents():
    return [a.info.model_dump() for a in AGENT_REGISTRY.values()]
