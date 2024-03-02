def fibo(x):
    if x <= 1:  # 0, 1의 경우
        return x
    return fibo(x - 2) + fibo(x - 1)

print(fibo(int(input())))  # n입력받아 fibo함수 호출