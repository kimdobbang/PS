y = int(input())

# # 오답
# if y % 4 == 0 & y % 100 != 0 :
#     print('1')
# elif y % 400 == 0 :
#     print('1')
# else :
#     print('0')


# # 정답1
# if (y % 4 == 0) & (y % 100 != 0) :
#     print('1')
# elif y % 400 == 0 :
#     print('1')
# else :
#     print('0')

# 정답2
if y % 4 == 0 and y % 100 != 0 :
    print('1')
elif y % 400 == 0 :
    print('1')
else :
    print('0')