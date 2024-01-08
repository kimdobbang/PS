n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(n):
    if numbers[i] == v:
        count += 1
print(count)