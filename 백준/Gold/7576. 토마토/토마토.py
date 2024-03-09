import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())  # 가로, 세로
arr = [list(map(int, input().split())) for _ in range(N)]  # 토마토 상자
q = deque()
visited = [[False] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]  # 상, 하, 좌, 우

# 시작점 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))
            visited[i][j] = True

# BFS
while q:
    i, j = q.popleft()

    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                q.append((nr, nc))
                arr[nr][nc] = arr[i][j] + 1

# 이차원 배열에서 최대값 출력(토마토 다 익는 최단 일수)
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, arr[i][j])

# 익지않은 토마토 존재여부 확인
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans = 0
            break

print(ans-1)