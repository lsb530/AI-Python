from get_client import client

model = 'gpt-4o-mini'

messages = [
    { "role": "user", "content": "2021년에 개봉한 공상 과학 영화를 알려주세요." },
    { "role": "system", "content": """
        1. 듄 (Dune)
        2. 핀치 (Finch)
        3. 더 어웨이크 (The Awake)
        4. 매트릭스: 리저렉션 (The Matrix Resurrections)
        5. 마더/안드로이드 (Mother/Android)
        6. 블리스 (Bbliss)
        7. 스완 송 (Swan Song)
    """ },
    { "role": "user", "content": "2021년에 개봉한 인기 영화를 알려주세요. "}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=300,
    # stop=["Human:", "AI:"]
    stop=["6."] # 5개만 나오게 하기
)

print(response.choices[0].message.content)