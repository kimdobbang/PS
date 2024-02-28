# 도화지는 100 * 100
# 색종이는 10 * 10
# a: 왼쪽변 ~ 도화지 왼쪽 변 사이 거리
# b: 색종이 아래쪽 변 ~ 도화지 아래쪽 변 사이 거리

N = int(input())
paper = [[False] * 100 for _ in range(100)]


for _ in range(N):
    # 1) 색종이 영역에 1 표기
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = True


# # 확인
# for i in paper:
#     print(*i)

# 2) 1을 카운트 => 넓이
# ans = 0
# for i in range(100):
#     for j in range(100):
#         if paper[i][j]:
#             ans += 1
#
# print(ans)

# 2-2) 1카운트 하는 다른 방법
ans = 0
for  lst in paper:
    ans += sum(lst)
print(ans)