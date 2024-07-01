a, b, c = map(int, input().split())
if a == b == c:
    print("*")
elif b == c:
    print("A")
elif c == a:
    print("B")
elif a == b:
    print("C")