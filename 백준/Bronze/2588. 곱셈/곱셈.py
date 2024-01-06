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