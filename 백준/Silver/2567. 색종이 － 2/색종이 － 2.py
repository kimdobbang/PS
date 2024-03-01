def count(r, c):
    dr = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dc = [0, 0, -1, 1]  # 상, 하, 좌, 우
    tmp_cnt = 0

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        # 1과 인접한 0 카운트
        if arr[nr][nc] == 0:
            tmp_cnt += 1
    return tmp_cnt


# 좌표 공간 생성
N = int(input())
arr = [[0]*101 for _ in range(101)]

for _ in range(N):
    X, Y = map(int, input().split())
    # 색종이 영역에 1 찍기
    for i in range(X, X + 10):
        for j in range(Y, Y + 10):
            arr[i][j] = 1

cnt = 0  # 둘레
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += count(i, j)
print(cnt)

# for line in arr:
    # print(*line)
