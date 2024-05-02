# 토끼

# stop = False
while True:

    key = int(input())
    # 0  나오면 멈춤
    if key == 0:
        break

    l, h = 1, 50
    while l <= h:
        m = l + (h - l) // 2  # (l + h)//2 도 같나???
        print(m, end=' ')

        if key == m:
            break
        elif key > m:
            l = m + 1
        else: # key < m
            h = m - 1
    print()