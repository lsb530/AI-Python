import click, os

from colorama import init
from gpt.get_client import client

init(autoreset=True)  # 자동 리셋

model = "gpt-4o"

base_messages = [
    { "role": "system", "content": "당신은 똑똑한 어시스턴트입니다. 답변은 명령줄(CLI)의 내용만 해주세요." },

    { "role": "user", "content": "현재 디렉토리의 모든 파일을 나열해주세요." },
    { "role": "assistant", "content": "ls -l" },

    { "role": "user", "content": "숨김 파일을 포함하여 현재 디렉터리의 모든 파일을 나열해주세요." },
    { "role": "assistant", "content": "ls -la" },

    { "role": "user", "content": "현재 디렉터리의 모든 파일을 삭제해 주세요." },
    { "role": "assistant", "content": "rm *" },

    { "role": "user", "content": "파일 'test.txt'에서 'sun'이라는 단어가 몇 번 등장하는지 세어 주세요." },
    { "role": "assistant", "content": "grep -o 'sun' test.txt | wc -l" }
]

while True:
    messages = base_messages.copy()

    request = input(
        click.style("Input (종료하려면 'quit' / 'q' 입력): ", fg="green")
    )

    if request.lower() in ["quit", "q"]:
        break

    messages.append({ "role": "user", "content": f"{request}" })

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=200,
        temperature=0
    )

    command = response.choices[0].message.content.strip()

    click.echo(
        click.style("Output: ", fg="yellow") + command
    )

    click.echo(
        click.style(
            "명령어를 실행하시겠습니까? (y/n): ", fg="blue"
        ),
        nl=False
    )

    choice = input()

    if choice.lower() == "y":
        r = os.system(command)
        if r != 0:
            click.echo(
                click.style("Error executing command.", fg="red")
            )
    elif choice == "n":
        click.echo()
        continue
    else:
        click.echo(
            click.style("잘못된 선택입니다. 'y' 또는 'n'을 입력해주세요.", fg="red")
        )

    click.echo()