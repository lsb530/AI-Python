from gpt.get_client import client

model = "gpt-4o-mini"

command = input('명령어 입력: ')

messages = [
    { "role": "system", "content": "당신은 똑똑한 어시스턴트입니다. 답변은 명령줄(CLI)의 내용만 해주세요." },

    { "role": "user", "content": "현재 디렉토리의 모든 파일을 나열해주세요." },
    { "role": "assistant", "content": "ls -l" },

    { "role": "user", "content": "숨김 파일을 포함하여 현재 디렉터리의 모든 파일을 나열해주세요." },
    { "role": "assistant", "content": "ls -la" },

    { "role": "user", "content": "현재 디렉터리의 모든 파일을 삭제해 주세요." },
    { "role": "assistant", "content": "rm *" },

    { "role": "user", "content": "파일 'test.txt'에서 'sun'이라는 단어가 몇 번 등장하는지 세어 주세요." },
    { "role": "assistant", "content": "grep -o 'sun' test.txt | wc -l" },

    # { "role": "user", "content": "현재 디렉터리의 파일 수를 세어주세요." },
    { "role": "user", "content": command },
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)
output = response.choices[0].message.content
print(output)