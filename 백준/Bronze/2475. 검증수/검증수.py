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

'''
SSAFY에서 함수 정의를 배워서 직접 활용해보려고 함수 사용하여 풀어봤다.
''
# 1 함수를 2개 합쳐서 쓰고싶은데,,, 아직 그렇게 못해서 그냥 2개의 함수를 정의하고 두번 적용했다.
numbers = list(map(int, input().split()))

def sqr(lst):
    return (i * i for i in lst)
    
# def func(lst2):
#     return sum(lst2) % 10
sol = lambda lst2: sum(lst2) % 10

print(sol(sqr(numbers)))



# 2   이건 위에서 내가 작성한 코드를 chat gpt가 수정해주었다.ㅎㅎ
def sqr_and_mod(numbers):
    squared_numbers = [i**2 for i in numbers]
    return sum(squared_numbers) % 10

numbers = list(map(int, input().split()))
result = sqr_and_mod(numbers)

print(result)
