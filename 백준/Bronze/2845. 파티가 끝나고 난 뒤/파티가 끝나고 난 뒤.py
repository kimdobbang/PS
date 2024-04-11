# 파티가 끝나고 난 뒤
L, P = map(int, input().split())
lst = list(map(int, input().split()))
res = L * P
for i in lst:
    print(i - res, end=' ')