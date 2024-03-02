## 피보나치수 5
n = int(input())

def yh_babo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return yh_babo(x - 2) + yh_babo(x - 1)

print(yh_babo(n))