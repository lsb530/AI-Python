from get_client import client

model = 'gpt-4o-mini'

# 출력의 접두어로 사용할 숫자 리스트
prefix = "\n\n1. "

messages = [
    {
        "role": "user",
        "content": f"세계 7대 불가사의는 무엇일까요?{prefix}"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)