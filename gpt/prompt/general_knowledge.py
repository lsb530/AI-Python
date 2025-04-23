from gpt.get_client import client

model = "gpt-4o-mini"

# 첫번째 프롬프팅 단계: 작업에 관한 지식생성
prompt = "올드 스쿨 랩의 가사적 특징과 주제에 관한 간결한 문장을 작성하세요."
messages = [
    { "role": "system", "content": "당신은 똑똑한 어시스턴트입니다." },
    { "role": "user", "content": prompt }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=200,
    temperature=0.5,
    stop=["assistant:", "user:"]
)
output = response.choices[0].message.content

# 두번째 프롬프팅 단계: 지식을 모델에 제공하고 출력을 생성
prompt = f"""배경: {output}

작업: 정의와 평등에 관한
올드 스쿨 랩 노래 가사를 작성하세요.
"""
messages = [
    { "role": "system", "content": "당신은 유명한 올드 스쿨 랩 작사가입니다." },
    { "role": "user", "content": prompt }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=500,
    temperature=1,
    stop=["assistant:", "user:"]
)
output = response.choices[0].message.content
print(
    "모델에 전달한 프롬프트는 다음과 같습니다"
    f":\n\n{prompt}"
)
print()
print(f"다음은 결과입니다.\n\n{output}")
