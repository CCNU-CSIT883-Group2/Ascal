from jinja2 import Template

choice_questions = Template(
    """
Role: Expert Teacher in "{{ subject }}"

Task: Generate some questions about "{{ tag }}" that meets the following requirements:

1. Question Type: "{{ type }}" with 4 options.
    - Options should contain only the content without labels like ‘A’, ‘B’, ‘C’, etc.
{%- if type == "Multi Choice" %}
    - There can be multiple correct answers(more than 1) if possible.
{%- endif %}
2. Answer and Explanation:
    - Provide concise and accurate answers and explanations.
3. Difficulty Level
    - Difficulty ranges from 1 to 5 (inclusive) in 0.1 increments; higher numbers indicate greater difficulty.
    - The difficulty number should be accurate.
4. Time Requirement:
    - Provide an appropriate time to answer the question as an integer in seconds.
5. Quantity:
    - Generate one question per request unless instructed with ‘next’.
6. Output Format:
    - Return the question in the specific JSON format provided below.
    - Return only the raw JSON string without any additional text.

JSON Format:

{
    "question": "String",
    "options": ["String", "String", "String", "String"],
    "answer": [Number],
    "explanation": "String",
    "difficulty": Number,
    "time_require": Number
}

Notes:
- question: The question text.
- options: An array of four option strings.
- answer: An array containing the index(es) of the correct option(s), starting from 0.
- explanation: Explanation for the answer.
- difficulty: The difficulty level as a number.
- time_require: Time to answer the question, in seconds.

Instructions:
- Ensure all elements are filled accurately.
- Do not include any extra text or formatting outside of the JSON.
- Focus on clarity and correctness.
- The question you generate should be unique.
    """
)

fill_in_the_blank_questions = Template(
    """
Role: Expert Teacher in "{{ subject }}"

Task: Generate some questions about "{{ tag }}" that meets the following requirements:

1. Question Type: fill in the blank questions
    - Options should contain only the content without labels like ‘A’, ‘B’, ‘C’, etc.
    - The blank that should be filled should be {% raw %}"{{ answer }}" like "The red {{ answer }} is delicious."{% endraw %}
    - The blank must present in the question, either at the beginning, middle, or end.
2. Answer and Explanation:
    - The answer should not be ambiguity if possible.
    - Provide concise and accurate answers and explanations.
3. Difficulty Level
    - Difficulty ranges from 1 to 5 (inclusive) in 0.1 increments; higher numbers indicate greater difficulty.
    - The difficulty number should be accurate.
4. Time Requirement:
    - Provide an appropriate time to answer the question as an integer in seconds.
5. Quantity:
    - Generate one question per request unless instructed with ‘next’.
6. Output Format:
    - Return the question in the specific JSON format provided below.
    - Return only the raw JSON string without any additional text.

JSON Format:

{
    "question": "String",
    "answer": "String",
    "explanation": "String",
    "difficulty": Number,
    "time_require": Number
}

Notes:
- question: The question text.
- answer: The answer text.
- explanation: Explanation for the answer.
- difficulty: The difficulty level as a number.
- time_require: Time to answer the question, in seconds.

Instructions:
- Ensure all elements are filled accurately.
- Do not include any extra text or formatting outside of the JSON.
- Focus on clarity and correctness.
- The question you generate should be unique.
    """
)
