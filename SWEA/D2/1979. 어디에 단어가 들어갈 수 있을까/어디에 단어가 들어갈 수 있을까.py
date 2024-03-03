def puzzle(word):
    ans = 0
    for i in range(N):
        cnt = 0
        # 행우선 탐색
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if arr[i][j] == 0 or j == N - 1:
                if cnt == word:
                    ans += 1
                cnt = 0

        # 열 우선 탐색
        for j in range(N):
            if arr[j][i]:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == word:
                    ans += 1
                cnt = 0

    return ans


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())  # N*N크기, K: 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc+1} {puzzle(K)}')
