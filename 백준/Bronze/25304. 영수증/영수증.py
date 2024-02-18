X = int(input())
N = int(input())

total = 0  # 총 금액 변수

# total 변수에 물건 금액 * 구매량 을 누적합
for i in range(N):
    price, amount = map(int, input().split())
    total += price * amount

# 결과 출력
if total == X:
    print('Yes')
else:
    print('No')
