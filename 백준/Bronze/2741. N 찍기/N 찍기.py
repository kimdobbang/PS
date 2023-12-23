N = int(input())

for i in range(1, N+1): # (시작값i, 끝값N) 1 이상 N+1 미만의 숫자 범위를 생성 123
# # for i in range(N): # (시작값0, 끝값N-1) 012 -> # print(i+1)해줘야 123출력
# for i in range(1, N): # (시작값1, 끝값N-1) 12
    print(i)
    
# for문 방법 두가지임! 
# N = int(input())
# for i in range(1, N+1):
#      print(i)

# N = int(input())
# for i in range(N):
#      print(i+1)

# 숏코딩
# print(*range(1,int(input())+1))