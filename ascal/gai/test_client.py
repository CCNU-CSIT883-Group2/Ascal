from dataclasses import dataclass
from faker import Faker
from enum import Enum

from .gai_instance import Instance

faker = Faker()


class TestQuestionType(Enum):
    Choice = "Choice"
    Blank = "Blank"


@dataclass(init=True)
class TestConfig:
    question_type: TestQuestionType


class TestClient(Instance):
    config: TestConfig

    def __init__(self, config: TestConfig) -> None:
        self.config = config

    def setup(self, requirement: str):
        pass

    def generate(self, prompt: str) -> str:
        import ascal.generator.model

        global question

        match self.config.question_type:
            case TestQuestionType.Choice:
                question = ascal.generator.model.ChoiceQuestion(
                    question=faker.sentence(),
                    options=[faker.word() for _ in range(4)],
                    answer=[faker.random_int(0, 3)],
                    explanation=faker.sentence(),
                    difficulty=float(faker.random_int(1, 5)),
                    time_require=faker.random_int(1, 5),
                )
            case TestQuestionType.Blank:
                question = ascal.generator.model.BlankQuestion(
                    question=faker.sentence(),
                    answer=faker.sentence(),
                    explanation=faker.sentence(),
                    difficulty=float(faker.random_int(1, 5)),
                    time_require=faker.random_int(1, 5),
                )

        return question.model_dump_json()
