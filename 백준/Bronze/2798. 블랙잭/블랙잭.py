import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))

max_sum = 0

for i in range(len(l)):
    for j in range(i+1, len(l)-1):
        for k in range(j+1, len(l)):
            temp_sum = l[i] + l[j] + l[k]
            if temp_sum <= m and temp_sum > max_sum:
                max_sum = temp_sum
print(max_sum)