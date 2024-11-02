from pydantic import BaseModel


class Question(BaseModel):
    question: str
    explanation: str
    difficulty: float
    time_require: int


class ChoiceQuestion(Question):
    options: list[str]
    answer: list[int]


class BlankQuestion(Question):
    answer: str
