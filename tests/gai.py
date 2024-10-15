from ascal import gai, generator

config = gai.TestConfig()

client = gai.Client(config)

generator = generator.ChoiceQuestionGenerator(
    "subject", "tag", generator.ChoiceType.Single, client
)

for question in generator.generate(5):
    print(question)
