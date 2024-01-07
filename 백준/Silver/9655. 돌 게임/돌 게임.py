# 이건 결과를 구하는 방법이 아니라,,,구해놓은 결과들 간의 규칙을 적은 듯 하다 그래서 다시 풀어봄.
n = int(input())
if n % 2:
    print("SK")
else:
    print("CY")

'''23.01.08 뭔가 너무 복잡하게 푼 것 같아서 다시 좀 정리 해봐야지'''

n = int(input()) # 돌 갯수 입력
dp = [-1] * 1001 # 리스트의 원소를 모두 -1로 초기화

dp[1] = 0 # SK
dp[2] = 1 # CY
dp[3] = 0

# 규칙에 따른 결과값 저장
for i in range(4,n+1):
    if dp[i - 1] == 1 or dp[i - 3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

# 결과 출력 (i는 지역변수라서 여기에 쓰면 안되는데 실수로 씀ㅜ n 써야함)
if dp[n] == 0:
    print("SK")
else:
    print("CY")
