dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]
for i in range(int(input())):
    print(dp[int(input())])

