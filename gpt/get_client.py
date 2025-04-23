import os
from openai import OpenAI

# 현재 디렉토리와 상위 디렉토리 경로 설정
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

# 가능한 경로 리스트 설정
possible_paths = [
    os.path.join(current_dir, 'chatgpt.env'),  # 현재 디렉토리
    os.path.join(parent_dir, 'chatgpt.env')   # 상위 디렉토리
]

# 실제로 존재하는 경로를 찾아서 변수 읽기
env_file_path = None
for path in possible_paths:
    if os.path.exists(path):
        env_file_path = path
        break

if env_file_path:
    # 환경 파일에서 API_KEY와 ORI_ID 같은 변수 읽기
    with open(env_file_path) as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value

    # API 키를 사용하여 OpenAI 클라이언트 초기화
    OPENAI_API_KEY = os.environ['API_KEY']
    client = OpenAI(api_key=OPENAI_API_KEY)
    # print(OPENAI_API_KEY[:5])
else:
    print("환경 파일을 찾을 수 없습니다.")