score, max_idx, max_score = 0, 0, 0  # 저장 변수 초기화

for i in range(5):
    score = sum(list(map(int, input().split())))
    # 최고점수와 우승자 번호 갱신
    if score > max_score:
        max_score = score
        max_idx = i + 1
print(max_idx, max_score)