N = list(map(int, input().split()))

temp = []
for n in N:
    temp.append(n**2)
print(sum(temp) % 10)

# 꼭 list가 필요햇던것은 아니다. 
# 그런데 무의식적으로 평소에 자주 쓰던 방법을 가져와 풀게되는 것 같다. 더 좋은 법 이 있어도ㅜ

# temp = 0
# for n in list(map(int, input().split())):
#     temp += n**2
# print(temp % 10)
