S = input()
counts = [0] * 26
for i in range(len(S)):
    counts[ord(S[i]) - 97] += 1

print(*counts)