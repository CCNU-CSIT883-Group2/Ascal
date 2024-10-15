from dataclasses import dataclass


@dataclass(init=True)
class ChatGPTConfig:
    api_key: str
    model: str
    endpoint: str = "https://api.openai.com/v1/chat/completions"
    max_token: int = 2048
