T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_height = max(trees)

    # 0 초기화
    even_cnt = odd_cnt = 0

    for height in trees:
        diff = max_height - height
        if diff % 2 == 1:
            odd_cnt += 1

        even_cnt += diff // 2

    while even_cnt >= odd_cnt + 2:
        even_cnt -= 1
        odd_cnt += 2

    day = max(even_cnt * 2, odd_cnt * 2 - 1)

    print(f"#{test_case} {day}")
