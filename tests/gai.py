import os

from ascal import gai, generator
from dotenv import load_dotenv

load_dotenv()

config = gai.KimiConfig(
    api_key=str(os.getenv("KIMI_API")),
    model="moonshot-v1-auto",
)

client = gai.Client(config)
generator = generator.ChoiceQuestionGenerator(
    "English", "noun", generator.ChoiceType.Multi, client
)

for question in generator.generate(1):
    print(question.model_dump_json(indent=2))
