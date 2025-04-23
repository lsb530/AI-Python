from get_client import client

model = 'gpt-4o-mini'

messages = [
    { "role": "system", "content": "당신은 똑똑하고 창의적인 어시스턴트입니다." },
    { "role": "user", "content": "한니발(Hannibal)은 누구인가요?" }
]

short_response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=50
)

long_response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=300
)

print('짧은 응답:')
print(short_response.choices[0].message.content)
print()
print('약간 긴 응답:')
print(long_response.choices[0].message.content)