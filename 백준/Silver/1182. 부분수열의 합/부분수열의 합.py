def f(idx, cnt, sum_v):  # idx: 탐색횟수, cnt: 부분수열크기, sum_v: 부분수열 합
    global ans

    # 모든 원소 탐색 완료한 경우
    if idx == N:
        # 부분수열 크기가 0이면
        if cnt <= 0:
            return
        # 원소의 합이 S와 같다면
        if sum_v == S:
            ans += 1  # 부분수열 갯수 1개 카운트
        return

    f(idx + 1, cnt + 1, sum_v + lst[idx])  # 부분수열 원소로 선택 한 경우
    f(idx + 1, cnt, sum_v)  # 부분수열 원소로 선택 안한 경우


N, S = map(int, input().split())
lst = list(map(int,input().split()))
ans = 0  # 부분수열 갯수
f(0, 0, 0)
print(ans)