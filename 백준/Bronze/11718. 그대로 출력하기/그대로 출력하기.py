# try except문으로 예외 처리 이용 (try, except문은 sys말고 input()사용함)

while True:
    try:
        print(input())
    except EOFError:
        break

        
        
        
'''
[코드 설명]
try 블록에서 sys.stdin.readline().rstrip()을 사용하여 한 줄을 읽어오고, 읽어온 값을 변수 n에 저장 후 출력함.
except 블록은 예외가 발생할 경우 실행됨. EOF 는 End Of File 의 줄임말로, 말 그대로 입력값이 없어지는 상황
즉, try 블록에서 값을 읽어오지 않는다면 실행됨.
input()은 EOF를 받을 때 EOFError를 일으키지만 sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴해서 sys 못씀(이건 if문 필요)

[처음보는 try, except 문법 메모]
try: 블록에 예외가 발생할 수 있는 코드 작성. 
만약 try 블록 안에서 예외가 발생하면 프로그램 실행이 즉시 try 블록에서 빠져나와 except 블록 실행됨

except: 예외가 발생했을 때 except 블록 실행됨. 구체적인 예외를 지정하지 않으면 모든 예외에 대해 처리함. 하지만 일반적으로는 발생할 수 있는 특정 예외를 명시하는게 좋음. 
여러개의 except 블록을 사용하여 다양한 예외에 대한 처리 가능(아래 예문 적어둠)
except Exception as e 는 모든 예외를 처리하며, 발생한 예외 객체를 'e'변수에 저장하여 활용할 수 있음
'''
# try:
#     n = int(input("정수를 입력하세요: "))
#     result = 10 / n
#     print("결과:", result)
# except ValueError:
#     print("정수를 입력해야 합니다.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except EOFError:
#     print("입력값이 없습니다..")
# except Exception as e:
#     print("예외가 발생했습니다:", e)




# # sys 쓰려면 반복문에 조건문을 이용
# import sys

# while True:
#     n = sys.stdin.readline().rstrip()

#     if not n:  # 더 이상 읽을 값이 없으면 루프 종료
#         break

#     print(n)

# '''
#  if not n:은 입력값이 빈 문자열인 경우를 확인합니다. 즉, 더 이상 읽을 값이 없을 때 루프를 종료합니다. 
#  이렇게 하면 사용자가 입력을 중지하거나 입력 스트림이 닫힐 때까지 계속해서 값을 읽고 출력합니다.
#  '''


# import sys

# while True:
#   s = sys.stdin.readline().rstrip()
#   if s == '':
#     break
#   else:
#     print(s)
    
# '''
#  sys.stdin.readline 함수를 사용하고 싶다면, 
#  EOFError를 발생시키지 않고 EOF를 빈 문자열로 받는 특성을 이용해 if 문으로 확인하는 위 방식으로 코드를 작성
#  '''
