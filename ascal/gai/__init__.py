"""
The GAI Client module provides a unified interface for interacting with the GAI instances.

For testing purposes, a `TestClient` is provided that generates random responses.
"""

from .openai.chatgpt import ChatGPTConfig
from .openai.kimi import KimiConfig
from .test_client import TestConfig
from .client import Client

__all__ = ["ChatGPTConfig", "KimiConfig", "TestConfig", "Client"]
