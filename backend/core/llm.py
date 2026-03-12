from openai import OpenAI
from anthropic import Anthropic
from groq import Groq
from core.config import get_settings


def get_openai() -> OpenAI:
    return OpenAI(api_key=get_settings().openai_api_key)


def get_anthropic() -> Anthropic:
    return Anthropic(api_key=get_settings().anthropic_api_key)


def get_groq() -> Groq:
    return Groq(api_key=get_settings().groq_api_key)


def chat_openai(messages: list, model: str = "gpt-4o", temperature: float = 0.7, stream: bool = False):
    client = get_openai()
    return client.chat.completions.create(
        model=model, messages=messages, temperature=temperature, stream=stream
    )


def chat_anthropic(messages: list, system: str = "", model: str = "claude-sonnet-4-20250514"):
    client = get_anthropic()
    return client.messages.create(
        model=model, max_tokens=4096, system=system, messages=messages
    )


def chat_groq(messages: list, model: str = "llama-3.3-70b-versatile", temperature: float = 0.7):
    client = get_groq()
    return client.chat.completions.create(
        model=model, messages=messages, temperature=temperature
    )
