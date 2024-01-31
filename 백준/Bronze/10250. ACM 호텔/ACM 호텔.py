T = int(input())

for tc in range(T):
    H, W, N = list(map(int, input().split()))

    # YY층
    if N % H == 0:
        YY = H
    else:
        YY = N % H

    # XX호
    if N % H == 0:
        XX = N // H
    else:
        XX = N // H + 1

    print((YY*100) + XX)