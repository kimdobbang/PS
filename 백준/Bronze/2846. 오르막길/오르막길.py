def is_empty(stack):
    if len(stack):
        return False
    return True


def max_h(stack):
    h = stack[-1] - stack[0]  # 오르막길 최대높이 계산
    return h


N = int(input())
arr = list(map(int, input().split()))
stk = []  # 스택
ans = 0  # 오르막길 없으면 0
for i in range(N):
    if is_empty(stk) or stk[-1] < arr[i]:       # 스택 비어있거나 top < i 면 스택에 추가
        stk.append(arr[i])
        if i == N-1:  # 마지막 값일 때도 처리
            if ans < max_h(stk):
                ans = max_h(stk)
    else:  # 둘다 아니면 최대 높이 구한 후에 스택 비우고 arr[i] 추가
        if ans < max_h(stk):
            ans = max_h(stk)
        stk.clear()
        stk.append(arr[i])

print(ans)
