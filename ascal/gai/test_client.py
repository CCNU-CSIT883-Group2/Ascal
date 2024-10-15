from dataclasses import dataclass
from faker import Faker

from .gai_instance import Instance

faker = Faker()


@dataclass
class TestConfig:
    pass


class TestClient(Instance):
    def __init__(self, config: TestConfig) -> None:
        pass

    def setup(self, requirement: str):
        pass

    def generate(self, prompt: str) -> str:
        import ascal.generator.model

        question = ascal.generator.model.ChoiceQuestion(
            question=faker.sentence(),
            options=[faker.word() for _ in range(4)],
            answer=[faker.random_int(0, 3)],
            explanation=faker.sentence(),
            difficulty=float(faker.random_int(1, 5)),
            time_require=faker.random_int(1, 5),
        )

        return question.model_dump_json()
