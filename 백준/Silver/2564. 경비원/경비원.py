w, h = map(int, input().split())  # 가로, 세로
n = int(input())  # 상점 수
dr = []  # 방향
ds = []  # 기준점에서 떨어진 거리
for i in range(n):
    r, s = map(int, input().split())  # dr에 방향, ds에 거리 append
    dr.append(r)
    ds.append(s)
xr, xs = map(int, input().split())  # 동근방향, 거리
# -------------------------------------------------------------
# 원점으로부터 거리
def distance(r, s):  # r: 방향, s:거리
    global w, h  # 여기서는 안해도 되는데, 애매할때는 global 쓰기.
    # 북
    if r == 1: return s
    # 동
    if r == 4: return w + s
    # 남
    if r == 2: return w + h + w - s
    # 서
    if r == 3: return (w + h) * 2 - s
#
# # 동근과 상점간 거리가 최소거리인지 판단
# def check_min(val):  # val: 동근과 상점간 거리(절대값)
#     global w, h
#     if val <= w + h:
#         return val
#     else:
#         return (w + h) * 2 - val

# total_min = 0
# for i in range(n):
#     res = abs(distance(xr, xs) - distance(dr[i], ds[i]))
#     total_min += check_min(res)
# print(total_min)

# 최소 거리인지 판단할때 check_min함수 안쓰고 아래처럼 조건문으로 처리해도 된다.
total_min = 0
for i in range(n):
    res = abs(distance(xr, xs) - distance(dr[i], ds[i]))
    if res > w + h:
        res = (w + h) * 2 - res
    total_min += res

print(total_min)
