import math
A, B, V = map(int, input().split())

# # ceil 함수
# result = (V - A)/(A - B) + 1
# print(math.ceil(result))

result = (V - A)/(A - B) + 1
# 형은 다르지만 값이 같다. ==는 값을 비교하나보다
if result == int(result):
    print(int(result))
else:
    print(int(result) + 1)



# # 분자 분모 나누어 떨어질 때 몫에다가 +1 또는 +2 (영호가 알려줌)
# if (V - A) % (A - B) == 0:
#     result = (V - A) // (A - B) + 1
# else:
#     result = (V - A) // (A - B) + 2
#
# print(result)