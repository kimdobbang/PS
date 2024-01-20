a = [1, 1, 2, 2, 2, 8]  # full set
n = list(map(int, input().split()))

print(*[ai - ni for ai, ni in zip(a, n)])

# for ai, ni in zip(a, n):
#     print((ai - ni), end=' ')


