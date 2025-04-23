import os

from gpt.get_client import client

text_file_path = os.path.relpath('./speech_ko.txt')
print(text_file_path)

audio_file_path = os.path.relpath('./speech_ko.mp3')
print(audio_file_path)

with open(text_file_path, 'r') as file:
    text = file.read()

voice_model = "tts-1"
voice_characters = [
    "alloy", "echo", "fable", "onyx", "nova", "shimmer"
]
# voice_character = "alloy"
voice_character = "echo"
# voice_character = "fable"
# voice_character = "onyx"
# voice_character = "nova"
# voice_character = "shimmer"

##### Deprecated Warning #####
# response = client.audio.speech.create(
#     model=voice_model,
#     voice=voice_character,
#     input=text
# )
# response.stream_to_file(audio_file_path)


# with client.audio.speech.with_streaming_response.create(
#     model=voice_model,
#     voice=voice_character,
#     input=text
# ) as response:
#     response.stream_to_file(audio_file_path)
# print(f"오디오가 {audio_file_path}에 저장되었습니다.")


for vc in voice_characters:
    dynamic_audio_file_path = os.path.relpath(f'./speech_ko({vc}).mp3')

    with client.audio.speech.with_streaming_response.create(
            model=voice_model,
            voice=vc,
            input=text
    ) as response:
        response.stream_to_file(dynamic_audio_file_path)

    print(f"오디오가 {dynamic_audio_file_path}에 저장되었습니다.")