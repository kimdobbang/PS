# 도화지는 100 * 100
# 색종이는 10 * 10
# a: 왼쪽변 ~ 도화지 왼쪽 변 사이 거리
# b: 색종이 아래쪽 변 ~ 도화지 아래쪽 변 사이 거리
# 색종이영역
# (3,17) (13, 17)
# (3, 7) (13, 7)
# (a, b+10) (a+10, b+10)
# (a, b) (a+10, b)

N = int(input())
paper = [[0] * 100 for _ in range(100)]

cnt = 0

# 색종이 영역에 1 입력
for i in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1


# # 확인
# for i in paper:
#     print(*i)

# 1을 카운트
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)