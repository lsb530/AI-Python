from get_client import client

model = 'gpt-4o-mini'

messages = [
    {
        "role": "system",
        "content": "당신은 똑똑하고 창의적이지만 장난끼 많은 AI입니다."
    },
    {
        "role": "user",
        "content": "ㅎㅇ. 오늘 저녁 메뉴 추천해줘. 맥주랑 같이 먹으면 좋을만한거!"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

# print(response)
print(response.choices[0].message.content)