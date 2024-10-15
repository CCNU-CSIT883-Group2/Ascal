from pydantic import BaseModel


class ChoiceQuestion(BaseModel):
    question: str
    options: list[str]
    answer: list[int]
    explanation: str
    difficulty: float
    time_require: int
