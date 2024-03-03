# import sys
# sys.stdin = open('1979_2.txt')

# 행 우선, 열 우선 탐색 -> arr에서 1이 k개인 것 카운트
def puzzle(N, word):
    ans = 0  # K가 들어갈 수 있는 칸의 갯수

    # 1) 행 우선 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:  # 값이 1인 경우
                cnt += 1
            else:  # 값이 1이 아닌 경우 조건 확인
                if cnt == word:
                    ans += 1
                cnt = 0
        if cnt == word:  # 행의 끝에서 조건 확인
            ans += 1
            cnt = 0

    # 2) 열 우선 탐색 (행의 끝에서 조건 확인을 아래 2번째 if문처럼 짤 수 있음 - 해찬)
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:  # 1일 때
                cnt += 1
            if arr[i][j] == 0 or i == N - 1:  # 0이거나 마지막 i에서 조건 검사
                if cnt == word:
                    ans += 1
                cnt = 0

    return ans


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())  # N*N크기, K: 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = puzzle(N, K)
    print(f'#{tc+1} {ans}')
    # for line in arr:
    #     print(*line)
    # print()
