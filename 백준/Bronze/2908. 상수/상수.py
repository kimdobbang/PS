A, B = input().split()

new_A = int(A[::-1])
new_B = int(B[::-1])

if new_A > new_B:
    print(new_A)
else:
    print(new_B)