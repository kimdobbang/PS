# 동전문제
# dp 배열 초기화
dp = [0] * 100
for i in range(10):
    dp[i] = i
for i in range(10, 25):
    dp[i] = min(dp[i-1] + 1, dp[i-10] + 1)
for i in range(25, 100):
    dp[i] = min(dp[i-1] + 1, dp[i-10] + 1, dp[i-25] + 1)


for _ in range(int(input())):
    P = int(input())
    # 테스트 케이스 100단위로 계싼
    res = 0
    while P > 0:
        res += dp[P % 100]
        P //= 100
    print(res)