import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 합배열 선언 및 생성
pre_sum = [0]  # index 맞추기 위한 0 세팅
tmp = 0
for i in lst:
    tmp += i
    pre_sum.append(tmp)
# print(pre_sum)

for i in range(M):
    s, e = map(int, input().split())
    s = s - 1  # 합배열이 0부터 시작하는데, 문제에서는 1로 간주함
    print(pre_sum[e] - pre_sum[s])