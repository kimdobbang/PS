def max_length():
    max_i, max_j = 0, 0  # 열, 행 우선 탐색하며 각각의 최대값 갱신

    # (1) 열 우선 탐색
    for i in range(N):
        cnt_j = 0  # 열 우선 탐색 하며 구한 유물 길이 초기화
        for j in range(M):
            if arr[i][j]:
                cnt_j += 1
                max_j = max(max_j, cnt_j)
            else: cnt_j = 0  # 0인 경우 초기화

    # (2) 행 우선 탐색
    for i in range(M):
        cnt_i = 0  # 열 우선 탐색 하며 구한 유물 길이 초기화
        for j in range(N):
            if arr[j][i]:
                cnt_i += 1
                max_i = max(max_i, cnt_i)
            else: cnt_i = 0

    return max(max_i, max_j)


T = int(input())

# 테스트 케이스 만큼 입력 받기
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 테스트 케이스 별 정답 출력
    ans = max_length()

    print(f'#{tc} {ans}')