N = int(input())
dp = [0]*(N+1)

dp[0],dp[1]= 2, 3

for i in range(2, N+1):
    dp[i] = dp[i-1] + 2**(i-1)
    
print(dp[N]**2)