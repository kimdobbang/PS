import sys; input = sys.stdin.readline
# 입력
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 합배열D 생성
D = [[0]*(N+1) for _ in range(N+1)]

# 합배열D 계산하여 채우기
for i in range(N):
    for j in range(N):
        D[i+1][j+1] = A[i][j] + D[i][j+1] + D[i+1][j] - D[i][j]

# 출력할 정답을 예시를 통해 알아낸 과정
# x1,y1    x2,y2
# 3, 3     4, 4
# ans = D[4][4] - D[2][4] - D[4][2] + D[2][2]
# ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

# 출력 값 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(ans)
