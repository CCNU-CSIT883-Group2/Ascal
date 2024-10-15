from abc import ABC, abstractmethod


class Instance(ABC):
    @abstractmethod
    def setup(self, requirement: str):
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
