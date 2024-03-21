# #  - (1) 파이프 설치 공간 확인: 벽 확인(조건문)
# #  - (2) 파이프 종류에 따른 dp 갱신
# #       설치공간 있어도 이전에 설치한 파이프가 어떤 것인지에 따라 놓지 못할 수 있음
# #  - (3) 출력
# # dp는 [가로][세로][대각선]에 대한 3차원 배열
# # dp[0][r][c] 가로
# # dp[1][r][c] 세로
# # dp[2][r][c] 대각선
def pipe():
    # 1행 처리
    dp[0][0][1] = 1  # 시작
    for i in range(2, N):
        if arr[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for r in range(1, N):
        for c in range(1, N):
            # 대각선 파이프를 dp[2][r][c]에 추가
            if arr[r][c] == 0 and arr[r-1][c] == 0 and arr[r][c-1] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
            # 가로, 세로 파이프를 dp[0][r][c]과 dp[1][r][c]에 추가
            if arr[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]  # 가로
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]  # 세로

    # 정답 출력
    print(sum(dp[i][N-1][N-1] for i in range(3)))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
pipe()
