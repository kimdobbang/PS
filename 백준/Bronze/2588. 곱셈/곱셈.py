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
# 1
a = int(input())
b = input()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B[0])*100+A*int(B[1])*10+A*int(B[2]))


#2
# 입력부
A = int(input())
B = list(map(int, list(input())))
# 출력부
print(A * B[2]) #3
print(A * B[1]) #4
print(A * B[0]) #5
print(A * B[0] * 100 + A * B[1] * 10 + A * B[2]) #6


#3
num1 = int(input())
num2 = int(input())
print(num1 * (num2 % 10))
print(num1 * (num2 % 100 // 10))
print(num1 * (num2 % 1000 // 100))
print(num1 * num2)


#4
a,b = int(input()), str(input())
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a*int(b))


#5
n1 = input()
n2 = input()
print(int(n1)*int(n2[2])) #3
print(int(n1)*int(n2[1])) #4
print(int(n1)*int(n2[0])) #5
print(int(n1)*int(n2)) #6
'''
