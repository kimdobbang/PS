# 입력
N = int(input())
arr = list(map(int, input().split()))

# dp배열: 작은 값으로 바꿔 적을거니가 N개 칸을 N으로 채움. 최대 N이라서
dp = [N] * 1100

# 계산
dp[0] = 0
for i in range(N):
    for j in range(1, arr[i] + 1):
        dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[N - 1] == N:
    print(-1)
else:
    print(dp[N - 1])