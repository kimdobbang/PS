N = int(input())
fac = 1

# 0이 아닌 N에 대한 N1 처리
for n in range(N, 0, -1): # 이렇게 범위설정으로 0입력되면 for문 돌지않고 1로 초기화한 fac 변수값 출력
    fac *= n
print(fac)