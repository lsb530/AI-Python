from get_client import client

model = 'gpt-4o-mini'

messages = [
    {
        "role": "user",
        "content":
            "다음을 포함하는 JSON형 반환"
            "0과 3사이의 소수(Primary numbers)"
    },
    {
        "role": "assistant",
        "content": """
            {
                "data": [2, 3, 5, 7],
                "length": 4,
                "smallest": 2,
                "largest": 7
            }
        """
    },
    {
        "role": "user",
        "content":
            "다음을 포함하는 JSON형 반환"
            "0과 6사이의 소수(Primary numbers)"
    },
    {
        "role": "assistant",
        "content": """
            {
                "data": [2, 3, 5],
                "length": 3,
                "smallest": 2,
                "largest": 5
            }
        """
    },
    {
        "role": "user",
        "content":
            "다음을 포함하는 JSON형 반환"
            "11과 65사이의 소수(Primary numbers)"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1.2
)

print(response.choices[0].message.content)