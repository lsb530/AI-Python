from gpt.get_client import client

model = 'gpt-4o-mini'

prefix = "옛날 옛적에 "

messages = [
    { "role": "system", "content": "당신은 이야기꾼입니다." },
    { "role": "user", "content": prefix },
]

response_high_frequency_penalty = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    frequency_penalty=2.0, # 높은 빈도 페널티 설정
)

response_low_frequency_penalty = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    frequency_penalty=0, # 낮은 빈도 페널티 설정
)

response_high_presence_penalty = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    presence_penalty=2.0, # 높은 존재 패널티 설정
)

response_low_presence_penalty = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=100,
    presence_penalty=0, # 낮은 존재 패널티 설정
)

content_high_frequency_penalty = response_high_frequency_penalty.choices[0].message.content
content_low_frequency_penalty = response_low_frequency_penalty.choices[0].message.content

content_high_presence_penalty = response_high_presence_penalty.choices[0].message.content
content_low_presence_penalty = response_low_presence_penalty.choices[0].message.content

print("높은 빈도 페널티:")
print(prefix + content_high_frequency_penalty)
print()
print("낮은 빈도 페널티:")
print(prefix + content_low_frequency_penalty)
print()

print("높은 존재 페널티:")
print(prefix + content_high_presence_penalty)
print()
print("낮은 존재 페널티:")
print(prefix + content_low_presence_penalty)