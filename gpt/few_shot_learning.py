from get_client import client

model = 'gpt-4o-mini'

messages=[
    {
        "role": "user",
        "content":
            "electrons dance the tango of uncertainty,"
            "entangling bits in a choreography that outpaces"
            "the swiftest supercomputers."
    },
    {
        "role": "assistant",
        "content":
            "Electrons Dance the Tango of Uncertainty,"
            "Entangling Bits in a Choreography That Outpaces"
            "the Swiftest Supercomputers."
    },
    {
        "role": "user",
        "content":
            "cloud architectures whisper across the sky,"
            "weaving a tapestry of data that blankets the digital"
            "landscape in a seamless symphony of bytes."
    },
    {
        "role": "assistant",
        "content":
            "Cloud Architectures Whisper Across the Sky,"
            "Weaving a Tapestry of Data That Blankets the Digital"
            "Landscape in a Seamless Symphony of Bytes."
    },
    {
        "role": "user",
        "content":
            "artificial Intelligence, the alchemist of the digital "
            "age, transmutes raw data into a golden labyrinth of"
            "insights, charting new territories in the realm of"
            "human thought."
    },
    {
        "role": "assistant",
        "content":
            "Artificial Intelligence, the Alchemist of the Digital "
            "Age, Transmutes Raw Data Into a Golden Labyrinth of"
            "Insights, Charting New Territories in the Realm of"
            "Human Thought."
    },
    {
        "role": "user",
        "content":
            "the internet of things is a vast ocean of data,"
            "a sea of information that ebbs and flows"
            "with the tides of time."
    }
]

# 대화 내용을 바탕으로 gpt-4o-mini 모델을 사용하여 응답 생성
# temperature 값을 1.2로 설정하여 다양한 응답 생성
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1.2
)

print(response.choices[0].message.content)