N, M = map(int, input().split())
# ij = [list(map(int, input().split())) for _ in range(M)]

arr = [i for i in range(1, N+1)]  # 바구니 번호
for m in range(M):  # M번 바꿈
    i, j = map(int, input().split())  # i, j할당
    back = reversed(arr[i-1:j])  # back 변수에 바꾼 값 넣고
    arr[i - 1:j] = back  # 원본의 동일한 부분에 back 적용

print(*arr)