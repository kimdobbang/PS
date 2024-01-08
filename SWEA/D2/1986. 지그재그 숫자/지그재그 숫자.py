T = int(input())

for t in range(1, T+1):
    N = int(input())
    sum = 0
    for n in range(1, N+1):
        if n % 2:
            sum += n
        else:
            sum -= n
    print(f'#{t} {sum}')