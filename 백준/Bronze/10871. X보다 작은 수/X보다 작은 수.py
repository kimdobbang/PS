import sys

n, x = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end = ' ')


# 내가 푼건데,,,위의 풀이가 더 맞는 것 같다. 아래는 n을 활용하지 않았음ㅜ 그리고 아래서 range(num)를 쓰지 않고 그냥 num이라고 써도 되네..??
# for i in num:
#     if i < x:
#         print(i, end = ' ')
# 공백으로 구분하여 출력해야하는데 처음에 end=' '를 몰라서 한 줄씩 출력 됐다.

''' 인덱스 쓰는경우
for i in range(n) :
    if num[i] < x :
        print(num[i], end = ' ')
'''
