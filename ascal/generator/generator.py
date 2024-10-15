from enum import Enum
from typing import Generator

from . import model
from . import prompts
from ..gai import client as Client


class ChoiceType(Enum):
    Single = "Single Chioce"
    Multi = "Multi Choice"


class ChoiceQuestionGenerator:
    subject: str
    tag: str
    type: ChoiceType
    client: Client.Client

    def __init__(self, subject: str, tag: str, type: ChoiceType, client: Client.Client):
        """
        return a new ChoiceQuestionGenerator object.

        Before generating questions, you need to set the client.
        """
        self.subject = subject
        self.tag = tag
        self.type = type
        self.client = client

    def __question_info(self) -> dict[str, str]:
        return {
            "subject": self.subject,
            "tag": self.tag,
            "type": self.type.value,
        }

    def generate(self, count: int) -> Generator[model.ChoiceQuestion, None, None]:
        """
        Generate questions.

        The return value is a generator that yields the generated questions.
        """

        if not self.client:
            raise ValueError("Client not set")

        self.client.setup(prompts.choice_questions.render(self.__question_info()))

        for _ in range(count):
            response = self.client.generate()
            yield model.ChoiceQuestion.model_validate_json(response)
