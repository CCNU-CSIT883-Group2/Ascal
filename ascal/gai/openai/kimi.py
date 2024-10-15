from dataclasses import dataclass


@dataclass(init=True)
class KimiConfig:
    api_key: str
    model: str
    endpoint: str = "https://api.moonshot.cn/v1/"
    max_token: int = 2048
