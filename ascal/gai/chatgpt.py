import openai

from dataclasses import dataclass
from .gai_instance import Instance


@dataclass
class ChatGPTConfig:
    api_key: str
    model: str
    endpoint: str

    def __init__(
        self,
        api_key: str,
        model: str,
        endpoint: str = "https://api.openai.com/v1/chat/completions",
    ):
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint


class ChatGPT(Instance):
    config: ChatGPTConfig
    history: list[dict[str, str]]
    client: openai.OpenAI

    def __init__(self, config: ChatGPTConfig):
        self.config = config
        self.history = []
        self.client = openai.OpenAI(
            api_key=config.api_key,
            base_url=config.endpoint,
        )

    def setup(self, requirement: str):
        self.history.append({"role": "system", "content": requirement})

    def generate(self, prompt: str) -> str:
        self.history.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.config.model,
            response_format={"type": "json_object"},
            messages=self.history,  # type: ignore
            max_tokens=2048,
            temperature=0.5,
        )

        content = response.choices[0].message.content
        if content is None:
            raise ValueError("Response content is None")

        self.history.append({"role": "assistant", "content": content})
        return content
