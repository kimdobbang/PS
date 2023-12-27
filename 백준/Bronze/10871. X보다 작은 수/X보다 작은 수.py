import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in a:
    if i < x:
        print(i, end=' ')
        # 공백으로 구분하여 출력해야하는데 처음에 end=' '를 몰라서 한 줄씩 출력 됐다.
