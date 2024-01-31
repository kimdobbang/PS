N = input()

# for i in range(0,len(N),10):
#     for j in range(i, min(i+10, len(N)-i)):
#         print(N[j], end='')

for i in range(0, len(N), 10):
    for j in range(i, min(i+10, len(N))):
        print(N[j], end='')
    print()
