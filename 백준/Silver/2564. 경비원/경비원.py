# 입력
w, h = map(int, input().split())  # 가로, 세로
n = int(input())  # 상점 수
dr = []  # 방향  [1, 3, 2]
ds = []  # 기준점에서 떨어진 거리 [4, 2, 8]
for i in range(n):
    r, s = map(int, input().split())  # dr에 방향, ds에 거리 append
    dr.append(r)
    ds.append(s)
xr, xs = map(int, input().split())  # 동근방향, 거리
# -------------------------------------------------------------
# 원점으로부터 동근의 거리
def x_loc(xr, xs):  # x: 동근방향, xs:동근 거리
    global w, h  # 여기서는 안해도 되는데, 애매할때는 global 쓰기.
    if xr == 1:  # 북
        return xs
    if xr == 4:  # 동
        return w + xs
    if xr == 2:  # 남
        return w + h + w - xs
    if xr == 3:  # 서
        return (w + h) * 2 - xs

# 원점으로부터 상점 거리
def distance(r, s):  # r: 방향, s:거리
    global w, h
    if r == 1:  # 북
        return s
    if r == 4:  # 동
        return w + s
    if r == 2:  # 남
        return w + h + w - s
    if r == 3:  # 서
        return (w + h) * 2 - s

# 동근과 상점간 거리가 최소거리인지 판단
def check_min(val):  # val: 동근과 상점간 거리(절대값)
    global w, h
    if val <= w + h:
        return val
    else:
        return (w + h) * 2 - val
# -------------------------------------------------------------
# 출력
# total_min = 0
# for i in range(n):
#     res = abs(x_loc(xr, xs) - distance(dr[i], ds[i]))
#     total_min += check_min(res)
# print(total_min)

# 최소 거리인지 판단할때는 check_min함수 안쓰고 이렇게 조건문으로 처리해도 된다.
total_min = 0
for i in range(n):
    res = abs(x_loc(xr, xs) - distance(dr[i], ds[i]))
    if res > w + h:
        res = (w + h) * 2 - res
    total_min += res

print(total_min)







''' 다른사람꺼 참고
W,H = map(int,input().split())
N = int(input())
shop_pnt = []
result = 0
for _ in range(N+1):
    a,b = map(int,input().split())
    if a == 1:
        shop_pnt.append([b,H])
    elif a== 2:
        shop_pnt.append([b,0])
    elif a == 3:
        shop_pnt.append([0,H-b])
    else:
        shop_pnt.append([W,H-b])
cur = shop_pnt.pop()
for shop in shop_pnt:
    if (cur[1] == H and shop[1] == 0) or (cur[1] == 0 and shop[1] == H):
        result += min(cur[0]+H+shop[0],W-cur[0]+H+W-shop[0])
    elif (cur[0] == W and shop[0] == 0) or (cur[0] == 0 and shop[0] == W):
        result += min(cur[1]+W+shop[1],H-cur[1]+W+H-shop[1])
    else:
        result += abs(cur[0]-shop[0])+abs(cur[1]-shop[1])
print(result)'''
