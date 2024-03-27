# 로또
def lotto(level):
    global pick_lst, used
    # 6개 선택 완료
    if level == 6:
        print(*pick_lst[1:])
        return

    # 6개 아니면 숫자 선택
    for i in range(level, k):
        # 사용하지 않은 숫자만(중복x)선택
        if not used[i] and pick_lst[level]< s[i]:
            used[i] = True
            pick_lst[level+1] = s[i]
            lotto(level + 1)
            used[i] = False

while True:
    k, *s = map(int, input().split())  # k: 집합 원소 수, s: 집합리스트
    if k == 0:break
    used = [False] * k
    pick_lst = [0] * 7
    lotto(0)
    print()
