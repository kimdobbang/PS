y = int(input())

# 제출_231223
if (y % 4 == 0 and y % 100 != 0) or y % 400 ==0:
    print("1")
else:
    print("0")

# 오답
# &를 쓰시고 싶으시다면 괄호를 이용하는 방법도 있습니다. 비트연산자와 혼동되기 때문에 보통은 윗분 말씀대로 and를 이용합니다.

# if y % 4 == 0 & y % 100 != 0 :
#     print('1')
# elif y % 400 == 0 :
#     print('1')
# else :
#     print('0')


# 정답1
# if (y % 4 == 0) & (y % 100 != 0) :
#     print('1')
# elif y % 400 == 0 :
#     print('1')
# else :
#     print('0')


# # 정답2
# if y % 4 == 0 and y % 100 != 0 :
#     print('1')
# elif y % 400 == 0 :
#     print('1')
# else :
#     print('0')
