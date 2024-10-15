from typing_extensions import overload
from typing import Union

from . import test_client, openai
from .gai_instance import Instance


GAIConfig = Union[openai.OpenAIConfig, test_client.TestConfig]


class Client:
    instance: Instance

    @overload
    def __init__(self, config: openai.OpenAIConfig) -> None: ...

    @overload
    def __init__(self, config: test_client.TestConfig) -> None: ...

    def __init__(self, config: GAIConfig) -> None:
        match config:
            case openai.chatgpt.ChatGPTConfig() | openai.kimi.KimiConfig():
                self.instance = openai.OpenAI(config)
            case test_client.TestConfig():
                self.instance = test_client.TestClient(config)

    def setup(self, requirement: str):
        self.instance.setup(requirement)

    def generate(self) -> str:
        return self.instance.generate("next")
