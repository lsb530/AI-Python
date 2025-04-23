from gpt.get_client import client

model = "gpt-4o-mini"

word = input('영어단어 입력: ')
prompt = f"단어 {word}의 품사를 결정하세요."

messages = [
    { "role": "system", "content": "당신은 똑똑한 어시스턴트입니다." },
    { "role": "user", "content": prompt }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)
output = response.choices[0].message.content
print(output)