import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if 0 < a and a < 10:
            print(a + b)
    except ValueError:
        break