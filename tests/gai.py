import os

from ascal import gai, generator
from dotenv import load_dotenv

load_dotenv()

config = gai.ChatGPTConfig(
    endpoint="https://www.gptapi.us/v1/chat/completions",
    api_key=str(os.getenv("GPT_API")),
    model="gpt-4o",
)

client = gai.Client(config)
generator = generator.BlankQuestionGenerator("Computer Network", "BGP", client)

for question in generator.generate(1):
    print(question.model_dump_json(indent=2))
