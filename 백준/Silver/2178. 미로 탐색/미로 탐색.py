# 그래프 이동 문제는 dr, dc 부터 만들기
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs():
    # 시작점 큐에 넣기
    visited[0][0] = 1  # 시작위치 0,0에 첫번째 방문 표시
    q = deque()
    q.append((0, 0))
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    
    # 큐 탐색하기
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 1 and visited[nr][nc] == False:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

bfs()
print(visited[N-1][M-1])