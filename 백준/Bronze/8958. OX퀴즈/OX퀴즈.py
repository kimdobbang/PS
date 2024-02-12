T = int(input())

for tc in range(T):
    case = input()
    total = 0
    score = 0
    for i in case:
        if i == 'O':
            score += 1
            total += score
        else:
            score = 0
    ans = total
    print(ans)
