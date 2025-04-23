import os
from openai import OpenAI

# .env 파일에서 API_KEY와 ORI_ID 같은 변수 읽기
with open("chatgpt.env") as env:
    for line in env:
        key, value = line.strip().split("=")
        os.environ[key] = value

# API 키를 사용하여 OpenAI 클라이언트 초기화
OPENAI_API_KEY = os.environ['API_KEY']
# print(OPENAI_API_KEY[:5])
client = OpenAI(api_key=OPENAI_API_KEY)
