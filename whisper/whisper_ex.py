import os

import whisper

# 필요에 따라 모델 설정 (ex: "tiny", "small", "medium", "large")
model_name = "medium"

try:
    model = whisper.load_model(model_name)
except Exception as e:
    print(f"모델 '{model_name}' 로드 에러: {e}")
    exit(1)

audio_file_path = "./audio/Buddy Hield speaking on Jimmys impact with the Warriors.mp3"

try:
    result = model.transcribe(
        audio=audio_file_path,
        language="en",
        fp16=False,
    )
    print("영어 변환 결과:")
    print(result)

    result = model.transcribe(
        audio=audio_file_path,
        language="zh",
        fp16=False
    )
    print("중국어 변환 결과:")
    print(result)

    result = model.transcribe(
        audio=audio_file_path,
        language="ja",
        fp16=False
    )
    print("일본어 변환 결과:")
    print(result)

    result = model.transcribe(
        audio=audio_file_path,
        language="ko",
        fp16=False
    )
    print("한국어 변환 결과:")
    print(result)

except Exception as e:
    print(f"오디오 파일 '{audio_file_path}' 필사 에러: {e}")
