# 내 풀이
N = int(input())
numbers = input()  # int로 받으면 for문으로 순회 불가

sum_n = 0
for number in numbers:
    sum_n += int(number)  # sum_n이 int형이라서 str인 number을 int로 변환
print(sum_n)


'''
내가 작성한 것은 아래의 코드보다 덜 암시적이고 명시적인 방법 같다.
그러나 입력 크기가 커지면 for반복문을 사용하고, 문자열 연산이 느리기 때문에 
반복문 없이 정수로 연산하는 방법을 고민해보면 좋겠다.
따라서 아래의 다른사람을 참고한 코드는 정수로 처리하여 sum()함수를 이용하기 때문에
더 효율적일 것 같다.
'''
# 다른 사람 풀이
# n = int(input())
# arr = list(map(int, input().strip()))
# print(sum(arr))
