def puzzle(N, word):
    ans = 0 
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else: 
                if cnt == word:
                    ans += 1
                cnt = 0
        if cnt == word:
            ans += 1
            cnt = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            if arr[i][j] == 0 or i == N - 1:
                if cnt == word:
                    ans += 1
                cnt = 0
    return ans
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = puzzle(N, K)
    print(f'#{tc+1} {ans}')
