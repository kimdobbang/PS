'''
<풀이>
1. 1 ~ 30으로 구성된 학생 전체 리스트 구성
2. 28줄의 과제 제출자 출석번호로 제출자 리스트 구성
3. 학생 전체 리스트를의 요소들 하나씩 꺼내서 과제 제출자 리스트에서 검사
     for ~ 개씩 꺼냄    
        if 학생i in 제출자: continue
        else: print(학생i)
학생1부터 학생30까지 모두 살펴볼 수 있다.
4. 원래 오름차순 정렬도 필요하지만 전체 학생리스트를 생성할 때 1부터 오름차순으로 생성했으며
이 생성 순서에 따라 탐색을 하고 조건에 맞는지 검사 후 출력하기 때문에 별도의 정렬 필요 없다.

<기억하기> 리스트 컴프리헨션
[(변수를 활용한 값) for (사용할 변수 이름) in (순회할 수 있는 값)]
(변수를 활용한 값) -> '실제로' 배열의 각 원소의 할당될 값
(사용할 변수 이름) -> 파이썬의 for 문에서 for과 in 사이에 for 블럭 안에서 사용될 인자의 이름(변수명)
                 -> for 키워드 왼쪽의 변수가 반복 가능한 객체(range(28)등)에서 값을 받는 변수
(순회할 수 있는 값) -> range처럼 값을 하나씩 살펴볼 수 있는 것을 총칭.
                      range 뿐만 아니라 다른 리스트, set, dict, tuple등도 될 수 있다.
                      일반 for문에서 쓸 수 있는 모든 값이 들어갈 수 있는 것
                      
submitters = [int(input()) for _ in range(28)]
 _는 루프 변수(i는 원래 표현에서 사용되지 않음)가 루프문에서 사용되지 않음을 나타내는 표현. 이는 가독성 주고 혼란 방지
'''

'''1'''
class_std = list(range(1,31))  # 리스트컴프리헨션 쓰지 않고 이렇게도 됨. 리컴 쓰는 이유는 안에서 수식,함수,조건을 추가할 수 있기 때문. 단순 숫자리스트는 이렇게 만들자
# submitters = int(input()) <- 정수로 인풋 받을건데 28번 받음
# submitters = []
# for i in range(28):
#     submitters.append(int(input()))

'''2'''
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