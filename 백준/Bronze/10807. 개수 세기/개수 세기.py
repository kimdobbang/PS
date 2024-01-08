n = int(input())
numbers = list(map(int, input().split()))
# Numlist = Numstr.split(' ') -> 처음본다?
v = int(input())
count = 0

# 처리
for i in numbers:
    if i == v:
        count += 1
print(count)

# for 문 돌리지않고 위 처리부를 주석처리 후 print(numbers.count(v))해도 됨
