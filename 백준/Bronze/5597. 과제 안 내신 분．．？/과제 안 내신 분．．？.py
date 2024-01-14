'''1'''
class_std = list(range(1,31))  # 리스트컴프리헨션 쓰지 않고 이렇게도 됨. 리스트컴프리헨션 이유는 안에서 수식,함수,조건을 추가할 수 있기 때문. 단순 숫자리스트는 이렇게 만들자

'''2'''
# submitters = int(input()) <- 정수로 인풋 받을건데 28번 받음
# submitters = []
# for i in range(28):
#     submitters.append(int(input()))
submitters = [int(input()) for i in range(28)]

'''3'''
# sub < std 이기 대문에 sub요소로 std검사하면안됨. 반대로 std요소를 꺼내 sub에 있나 확인
for i in class_std:
    if i not in submitters:  # not in 이 코드도 직관적이고 짧았다.(아래 in 남겨둠)
        print(i)
        
# for i in class_std:
#     if i in submitters:
#     else:
#         print(i)
