arr = [[0]*100 for _ in range(100)]

# 입력
for i in range(4):
    rec = list(map(int, input().split()))
    lx, ly = rec[0], rec[1]
    rx, ry = rec[2], rec[3]

    for x in range(lx, rx):
        for y in range(ly, ry):
            arr[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if (arr[i][j] == 1):
            cnt += 1

print(cnt)