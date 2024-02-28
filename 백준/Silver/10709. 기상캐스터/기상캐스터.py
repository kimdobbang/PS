H, W = map(int, input().split()) # 구역
arr = [[-1] * W for _ in range(H)]
cast = [input() for _ in range(H)]  # 문자열 H개 주어짐

for i in range(H):
    c = False  # c 만나면 True로 바뀌고, 조건문에서 True일때 앞의 값에 1씩 더해준 값을 새로운 배열에 넣어줌.
    for j in range(W):
        if c == True:
            arr[i][j] = arr[i][j-1] + 1
        if cast[i][j] == 'c':
            arr[i][j] = 0
            c = True

# 출력
for line in arr:
    print(*line)
