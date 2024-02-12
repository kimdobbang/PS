N = int(input())
# 점수 리스트
score = list(map(int, input().split()))
# 최대값 M 도출
M = score[0]
for i in range(len(score)):
    if score[i] > M:
        M = score[i]
# 모든 점수/M * 100로 변환 합계을 통해 평균 출력
total = 0
for i in range(len(score)):
    total += score[i] / M * 100
print(total / N)
