def round1(ac, bc):     # [ 0, 1, 2, 3, 4]
    if ac[4] > bc[4]:
        return 'A'
    elif ac[4] < bc[4]:
        return 'B'
    else:
        pass

    if ac[3] > bc[3]:
        return 'A'
    elif ac[3] < bc[3]:
        return 'B'
    else:
        pass

    if ac[2] > bc[2]:
        return 'A'
    elif ac[2] < bc[2]:
        return 'B'
    else:
        pass

    if ac[1] > bc[1]:
        return 'A'
    elif ac[1] < bc[1]:
        return 'B'
    else:
        return 'D'

N = int(input())  # 총 라운드 수
for tc in range(N):
    a, *a_info = map(int, input().split())  # a딱지 그림 수, 딱지 그림
    b, *b_info = map(int, input().split())  # b딱지 그림 수, 딱지 그림

    # 각자의 카운트배열 생성
    a_cnt = [0] * 5
    b_cnt = [0] * 5
    for i in a_info:
        a_cnt[i] += 1
    for j in b_info:
        b_cnt[j] += 1

    print(round1(a_cnt, b_cnt))