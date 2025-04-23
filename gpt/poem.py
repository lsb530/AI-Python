from get_client import client

completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {'role': 'user', 'content': 'AI에 대한 시를 하나 작성해 줘'}
    ]
)

print(completion.choices[0].message.content)