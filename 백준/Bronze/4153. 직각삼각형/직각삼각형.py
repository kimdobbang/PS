while True:
    arr = list(map(int, input().split()))
    # 정렬 하려고 했는데, 피타고라스 정리 특성상 제일 큰 하나(빗변)만 찾으면 될 듯
    if arr[0] == 0:
        break
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    arr[0], arr[max_idx] = arr[max_idx], arr[0]

    if arr[0]**2 == arr[1]**2 + arr[2]**2:
        print('right')
    else:
        print('wrong')