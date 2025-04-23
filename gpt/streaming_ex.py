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
    max_tokens=200,
    stream = True
)

print(prefix, end="")

for message in response:
    content = message.choices[0].delta.content
    if content:
        print(content, end="")
