C = int(input())

for tc in range(C):
    lst= list(map(int,input().split()))
    n, *score_lst = lst
    avg = sum(score_lst) / n

    cnt = 0
    for i in range(len(score_lst)):
        if score_lst[i] > avg:
            cnt += 1
        ans = round(cnt / n * 100, 3)
        
    print(f'{ans}%')