import math

def is_prime(x):
    global result
    cnt = 0
    
    if x == 1:  # 1은 소수 아님
        return

    for i in range(2, int(math.sqrt(x))+1):  #  x가 2 ~ (x-1) 까지의 수로 나눠 떨어지는지
        if x % i == 0:  # 나눠 떨어지면 소수 아님
            cnt += 1
    if cnt == 0:  # 소수아님이 판별된 횟수 0이면,, 소수 하나 있다!
        result += 1

n = int(input())
lst = list(map(int, input().split()))
result = 0
for i in range(n):
    is_prime(lst[i])
print(result)

# 더 좋고 깔끔한 풀이가 있을 것 같은데 좀 구리게 푼 것 같다. 푸느라 급급해서 ㅠㅠ 다른 풀이도 찾아봐야지