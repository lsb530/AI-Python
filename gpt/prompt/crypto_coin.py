from gpt.get_client import client

crypto = input("암호화폐 이름을 입력해주세요 : ")

model = "gpt-4o-mini"

messages = [
    { "role": "system", "content": "당신은 똑똑한 어시스턴트입니다. 아래 답변 형식에 맞추어 모르는 것은 검색해서 알려주세요." },
    { "role": "user", "content": "Bitcoin" },
    { "role": "assistant", "content": (
        "- BTC는 2008년에 생성되었습니다.\n"
        "- 자세한 정보는 여기서 확인할 수 있습니다.\n"
        "https://bitcoin.org/en/\n"
        "- 최신 가격은 여기서 확인할 수 있습니다.\n"
        "https://coingecko.com/en/coins/bitcoin\n"
        "- 최고가는 $64,895.00입니다.\n"
        "- 최저가는 $67.81입니다.\n"
    ) },
    { "role": "user", "content": "Ethereum" },
    { "role": "assistant", "content": (
        "- ETH는 2015년에 생성되었습니다.\n"
        "- 자세한 정보는 여기서 확인할 수 있습니다.\n"
        "https://ethereum.org/en\n"
        "- 최신 가격은 여기서 확인할 수 있습니다.\n"
        "https://coingecko.com/en/coins/ethereum\n"
        "- 최고가는 $4,362.35입니다.\n"
        "- 최저가는 $0.43입니다.\n"
    ) },
    { "role": "user", "content": "Dogecoin" },
    { "role": "assistant", "content": (
        "- ETH는 2013년에 생성되었습니다.\n"
        "- 자세한 정보는 여기서 확인할 수 있습니다.\n"
        "https://dogecoin.com\n"
        "- 최신 가격은 여기서 확인할 수 있습니다.\n"
        "https://coingecko.com/en/coins/dogecoin\n"
        "- 최고가는 $0.73입니다.\n"
        "- 최저가는 $0.00008690입니다.\n"
    ) },
    { "role": "user", "content": "crypto" }
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
)

output = response.choices[0].message.content
print(output)