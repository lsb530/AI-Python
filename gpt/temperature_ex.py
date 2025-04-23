from gpt.get_client import client

model = 'gpt-4o-mini'

prefix = "옛날 옛적에 "

messages = [
    { "role": "system", "content": "당신은 이야기꾼입니다." },
    { "role": "user", "content": prefix },
]

response_high_temperature = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    temperature=2,
    stop=["\n",]
)
content_high_temperature = response_high_temperature.choices[0].message.content

response_medium_temperature = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    temperature=1,
    stop=["\n",]
)
content_medium_temperature = response_medium_temperature.choices[0].message.content

response_low_temperature = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    temperature=0,
    stop=["\n",]
)
content_low_temperature = response_low_temperature.choices[0].message.content

# high: 문맥과 관련이 없는 내용이 많이 생성되고 부정확한 정보가 포함됨
print(f"""
1. 높은 temperature:
{prefix}{content_high_temperature}
""")

# medium: 문맥에 맞는 응답이 생성되며 창의적이지만 너무 파격적이지는 않음
print(f"""
2. 중간 temperature:
{prefix}{content_medium_temperature}
""")

# low: 문맥에 맞는 응답이 생성되지만 매우 결정론적이어서 예측 가능성이 높음
print(f"""
3. 낮은 temperature:
{prefix}{content_low_temperature}
""")