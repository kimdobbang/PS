from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
q = deque()


def bfs(s):
    q.append(s)
    visited[s] = True
    while q:
        now = q.popleft()
        for next in lst[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


# 인접리스트
for i in range(1, M+1):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

# bfs dfs 모든 곳 다 탐색하기 위해
# bfs 호출한 횟수가 연결요소의 개수
visited = [False] * (N + 1)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
