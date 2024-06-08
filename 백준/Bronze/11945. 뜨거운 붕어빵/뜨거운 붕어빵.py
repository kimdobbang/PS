n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m-1, -1, -1):
        print(lst[i][j], end="")
    print()
