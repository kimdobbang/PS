w, h = map(int, input().split())
n = int(input())
dr, ds = [], []
for i in range(n):
    r, s = map(int, input().split())
    dr.append(r)
    ds.append(s)
xr, xs = map(int, input().split())
def x_loc(xr, xs):
    if xr == 1: return xs
    if xr == 4: return w + xs
    if xr == 2: return w + h + w - xs
    if xr == 3: return (w + h) * 2 - xs
def dis(r, s):
    if r == 1: return s
    if r == 4: return w + s
    if r == 2: return w + h + w - s
    if r == 3: return (w + h) * 2 - s
def check(val):
    if val <= w + h: return val
    else: return (w + h) * 2 - val
total = 0
for i in range(n):
    res = abs(x_loc(xr, xs) - dis(dr[i], ds[i]))
    total += check(res)
print(total)