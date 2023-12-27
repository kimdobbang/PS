# i 범위를 0부터 8까지 지정후 i에 1씩 더해짐 따라서 i= 1 ~ 9 되어 위의 range(1,10)과 동일 효과
#N = int(input())
#for i in range(9):
#    i += 1
#    result = f'{N} * {i} = {N * i}'
#    print(result)
    
# #(다른 방법 도전) i 범위를 1부터 9까지 지정. i는 이미 1로 시작하므로 변수 초기화 불필요
# N = int(input())
# for i in range(1, 10):
#     result = f'{N} * {i} = {N * i}'
#     print(result) 

    
#남의 풀이 (이렇게 하는게 가장 좋은 듯 range(9)하니 변수초기화 해야하고 덜 직관적)
import sys
n = int(sys.stdin.readline())
for i in range(1, 10):
    print('{} * {} = {}'.format(n,i, n*i))
#print(f'{n} * {i} = {n*i}')
