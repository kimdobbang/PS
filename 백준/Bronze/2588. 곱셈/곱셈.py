# 왜 리스트에 담았나 쓸데없이
a = int(input())
b = input()
b_int = int(b)
b_list = list(map(int,b))
# b_list = [int(a) for a in b]

c = a*b_list[2]
d = a*b_list[1]
e = a*b_list[0]
f = c + d*10 + e*100

print(c)
print(d)
print(e)
print(f)

'''
남들꺼 보고 공부하자.
# # 1
# A = int(input()) #1
# B = input() #2
# print(A * int(B[2])) #3
# print(A * int(B[1])) #4
# print(A * int(B[0])) #5
# print(A * int(B)) #6

#2 몫과 나머지를 이용
# num1 = int(input()) #1
# num2 = int(input()) #2
# print(num1 * (num2 % 10)) #3
# print(num1 * (num2 % 100 // 10)) #4
# print(num1 * (num2 % 1000 // 100)) #5 385를 1000으로 나눈 몫0, 나머지 385이므로  num2 //100와 같다.
# # print(num1 * (num2 //100))
# print(num1 * num2) #6


#3 반복문
A = int(input())
B = input()
for i in range(2, -1, -1) :
    print(A * int(B[i]))
print(A * int(B))

'''
