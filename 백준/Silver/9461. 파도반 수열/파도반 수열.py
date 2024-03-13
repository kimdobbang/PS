import sys
input = sys.stdin.readline

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
# dp[6] = dp[6-1] + dp[6-5]
# dp[100] = dp[100-1] + dp[100-5]
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]


# 100이 아니라 숫자가 컸다면 테스트 케이스를 한꺼번에 모두 받아서 최대값 만큼 까지만 구할 수 있다
for i in range(int(input())):
    print(dp[int(input())])
