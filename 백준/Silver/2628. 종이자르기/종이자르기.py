# 최대 사각형 넓이 구하는 함수
def max_sqr():
    i_max = 0
    j_max = 0
    for i in range(1, len(I)):
        if i_max < I[i] - I[i-1]:
            i_max = I[i] - I[i-1]

    for j in range(1, len(J)):
        if j_max < J[j] - J[j-1]:
            j_max = J[j] - J[j-1]
    
    return i_max * j_max


W, H = map(int, input().split())  # 가로, 세로
L = int(input())  # 점선 수
I, J = [0], [0]  # I: 가로로 자르는 선 J: 세로로 자르는 선 위치 <- 시작점 0 넣고 시작

# 가로로 잘리는 곳 I에 추가, 세로로 잘리는 곳 J에 추가
for _ in range(L):
    T, N = map(int, input().split())  # 타입(J: 1, I: 0), N: 번호
    if T: J.append(N)
    else: I.append(N)
I.append(H), J.append(W)  # 종이 맨 마지막
I.sort(), J.sort()  # 정렬

print(max_sqr())
