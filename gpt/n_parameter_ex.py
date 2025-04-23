from gpt.get_client import client

model = 'gpt-4o-mini'

prefix = "옛날 옛적에 "

messages = [
    { "role": "system", "content": "당신은 이야기꾼입니다." },
    { "role": "user", "content": prefix },
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    n = 2,
    stop = ["\n"]
)

choices = response.choices
for choice in choices:
    print(f"Choice: {choice.index}")
    print(prefix + choice.message.content)
    print()
