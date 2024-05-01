# 크로아티아 알파벳

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

W = input()

# ans = len(W)

for i in lst:
    W = W.replace(i,'0')
print(len(W))


#
# while True:
#
#     for i in lst:
#         if i in W:
#             ans = ans - len(i) + 1
#             W.replace(i, '')
#
# print(ans)