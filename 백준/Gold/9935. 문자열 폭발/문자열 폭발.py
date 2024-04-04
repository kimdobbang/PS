import sys; input = sys.stdin.readline
str = list(input().rstrip())
check = list(input().rstrip())

stack = []
for i in str:
    stack.append(i)
    if stack[-len(check):] == check: # 폭탄문자열과 같은지 뒤부터 len(폭탄문자열) 만큼 확인하여 삭제
        del stack[-len(check):]

# 반복문 종료 후 출력
if stack:
    #for i in stack:
    #    print(*i,end='')
    print(''.join(stack))
else:
    print("FRULA")
