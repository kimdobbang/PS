import sys
a, b = map(int, sys.stdin.readline().split())


def cal(a, b):
    return a**2 - b**2


print(cal(a, b))
