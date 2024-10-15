from typing_extensions import overload
from typing import Union

from . import chatgpt, test_client
from .gai_instance import Instance


GAIConfig = Union[chatgpt.ChatGPTConfig, test_client.TestConfig]


class Client:
    instance: Instance

    @overload
    def __init__(self, config: chatgpt.ChatGPTConfig) -> None: ...

    @overload
    def __init__(self, config: test_client.TestConfig) -> None: ...

    def __init__(self, config: GAIConfig) -> None:
        match config:
            case chatgpt.ChatGPTConfig():
                self.instance = chatgpt.ChatGPT(config)
            case test_client.TestConfig():
                self.instance = test_client.TestClient(config)

    def setup(self, requirement: str):
        self.instance.setup(requirement)

    def generate(self) -> str:
        return self.instance.generate("next")
