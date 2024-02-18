N, M = map(int, input().split())

# N개 바구니 배열 생성
basket = [0] * (N+1)

# 공 넣는 횟수 M번 반복하며 i, j, k 값 받기
for _ in range(M):
    i, j, k = map(int, input().split())

    # i번째 바구니부터 j번째 바구니까지 k 넣기
    for i in range(i, j+1):
        basket[i] = k

# 바구니 내부를 확인하기위해 출력하기
for i in basket[1:]:
    print(i, end=' ')

# 인덱스 넘 어려웡