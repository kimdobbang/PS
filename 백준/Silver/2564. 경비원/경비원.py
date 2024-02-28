w, h = map(int, input().split())
n = int(input())
dr = []
ds = []
for i in range(n):
    r, s = map(int, input().split())
    dr.append(r)
    ds.append(s)
xr, xs = map(int, input().split())
# 원점부터 거리 계산
def distance(r, s):
    # 북
    if r == 1: return s
    # 동
    if r == 4: return w + s
    # 남
    if r == 2: return w + h + w - s
    # 서
    if r == 3: return (w + h) * 2 - s
# 결과
total_min = 0
for i in range(n):
    res = abs(distance(xr, xs) - distance(dr[i], ds[i]))
    if res > w + h:
        res = (w + h) * 2 - res
    total_min += res
print(total_min)