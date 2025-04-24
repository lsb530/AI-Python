def apply_custom(filename):
    # 파일 읽기 (파일에 이미 "번호. 이름" 형식으로 되어 있다고 가정)
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    total = len(lines)
    cols = 3
    # 행(row) 수 계산 (총 항목을 3열로 나누기)
    rows = (total + cols - 1) // cols

    # 각 열(column)에 들어갈 문자열의 최대 길이 계산
    max_len = max(len(lines[i]) for i in range(total))

    # 3열로 가로 정렬하여 출력
    for r in range(rows):
        row_items = []
        for c in range(cols):
            idx = c * rows + r
            if idx < total:
                # 각 항목을 max_len에 맞춰 왼쪽 정렬
                row_items.append(lines[idx].ljust(max_len))
        print("    ".join(row_items))

        # 올바른 입력이 들어올 때까지 반복
    while True:
        try:
            choice = None
            if 'artist' in filename:
                choice = input("\n원하는 작가의 번호를 입력하세요: ").strip()
            elif 'style' in filename:
                choice = input("\n원하는 아트 스타일의 번호를 입력하세요: ").strip()
            num = int(choice)
            if 1 <= num <= total:
                break
            else:
                print("❗ 잘못된 번호입니다. 1부터", total, "사이의 숫자를 입력해주세요.")
        except ValueError:
            print("❗ 숫자를 입력해주세요.")

        # 선택한 작가 이름만 출력
    _, name = lines[num - 1].split('. ', 1)
    # print(f"\n선택한 작가: {name}")

    return name
