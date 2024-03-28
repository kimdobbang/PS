# 별찍기 -7
def recur(N, i):
    M = 2 * N - 1  # 출력할 줄 갯수, 한 줄당 출력 갯수

    # 종료조건
    if i > M:
        return

    # 출력 할 공백과 * 갯수
    if i < N:
        star = i * 2 -1
        blank = (M - star) // 2
        # blank = N - i
        # star = M -(blank * 2)
        
    else:  # i >= N
        blank = i - N
        star = M - (blank * 2)
    ans = (' ' * blank) + ('*' * star)
    print(ans)

    # 재귀 호출
    recur(N, i + 1)

recur(int(input()), 1)
