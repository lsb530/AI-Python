from get_client import client

model = 'gpt-4o-mini'

messages = [
    { "role": "system", "content": "당신은 똑똑하고 창의적인 어시스턴트입니다." },
    { "role": "user", "content": "한니발(Hannibal)은 누구인가요?" }
]

# 300 토큰까지 중단하지 않고, \n을 만날때까지 계속 진행
response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=300,
    stop=["\n", "Human:", "AI:"] # 출력 중단 시퀀스 설정(줄바꿈, 'Human:', 'AI:')
)

print(response.choices[0].message.content)
