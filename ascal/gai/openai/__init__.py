"""
GAI Client that shares OpenAI like interface.
"""

import openai

from typing import Union
from ..gai_instance import Instance
from .chatgpt import ChatGPTConfig
from .kimi import KimiConfig

OpenAIConfig = Union[ChatGPTConfig, KimiConfig]


class OpenAI(Instance):
    config: OpenAIConfig
    history: list[dict[str, str]]
    client: openai.OpenAI
    token_used: int = 0

    def __init__(self, config: OpenAIConfig):
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
            max_tokens=self.config.max_token,
            temperature=0.5,
        )

        content = response.choices[0].message.content
        assert content is not None, ValueError("Response content is None")

        usage = response.usage
        assert usage is not None, ValueError("Response usage is None")

        self.token_used += usage.total_tokens
        self.history.append({"role": "assistant", "content": content})
        return content


__all__ = ["OpenAI", "ChatGPTConfig", "KimiConfig"]
