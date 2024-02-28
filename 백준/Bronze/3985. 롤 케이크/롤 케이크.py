L = int(input())  # 롤케이크 길이
N = int(input())  # 방청객 수
roll = [0] * (L+1)  # 롤케이크

#  (ans1) 가장 많이 받으리라 기대되는 방청객
max_v = 0
for i in range(1, N+1):
    P, K = map(int, input().split())
    if max_v < K - P:  # 조건을 만족하는 방청객 복수일 땐 가장 작은 i값 출력하기 위해 등호는 뺌
        max_v = K - P
        ans1 = i

    # 롤케이크 찜하기
    for j in range(P, K+1):
        if roll[j] == 0:
            roll[j] = i
# print(roll)

# (ans2) 실제 젤 많이 받은 방청객 찾기
max_c = 0
for i in range(1, L+1): # 방청객 번호
    cnt = 0  # 케이크에 적힌 방청객 번호 카운트 (방청객마다 초기화)
    for j in range(1, len(roll)):  # 방청객 번호 적힌 롤케이크 range(1,11)이므로 1~10
        if roll[j] == i:  # 적힌 번호가 방청객 번호랑 같을 때
            cnt += 1
            if max_c < cnt:
                max_c = cnt
                ans2 = i

print(ans1)
print(ans2)
