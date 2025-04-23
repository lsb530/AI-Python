from get_client import client

model = 'gpt-4o-mini'

messages = [
    { "role": "system", "content": "당신은 똑똑하고 창의적인 어시스턴트입니다." },
    { "role": "user", "content": "한니발(Hannibal)은 누구인가요?" }
]

stop_token = "."

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=50,
    stop=[stop_token]
)

print(response.choices[0].message.content + stop_token)
