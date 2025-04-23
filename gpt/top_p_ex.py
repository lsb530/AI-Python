from gpt.get_client import client

model = 'gpt-4o-mini'

prefix = "옛날 옛적에 "

messages = [
    { "role": "system", "content": "당신은 이야기꾼입니다." },
    { "role": "user", "content": prefix },
]

response_high_topp = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    top_p=1,
    stop=["\n",]
)
content_high_topp = response_high_topp.choices[0].message.content

response_medium_topp = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    top_p=0.5,
    stop=["\n",]
)
content_medium_topp = response_medium_topp.choices[0].message.content

response_low_topp = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    top_p=0.1,
    stop=["\n",]
)
content_low_topp = response_low_topp.choices[0].message.content

print(f"""
1. 높은 topp:
{prefix}{content_high_topp}
""")

print(f"""
2. 중간 topp:
{prefix}{content_medium_topp}
""")

print(f"""
3. 낮은 topp:
{prefix}{content_low_topp}
""")