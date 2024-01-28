# without built-in function

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c :
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    lst = [a, b, c]
    max_val = lst[0] 
    for i in lst:
        if i > max_val:
            max_val = i
    print(max_val * 100)  