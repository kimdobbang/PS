N = int(input())

# # i 범위를 1부터 9까지 지정. i는 이미 1로 시작하므로 변수 초기화 불필요
# for i in range(1, 10):
#     result = f'{N} * {i} = {N * i}'
#     print(result) 

 # i 범위를 0부터 8까지 지정후 i에 1씩 더해짐 따라서 i= 1 ~ 9 되어 위의 range(1,10)과 동일 효과
for i in range(9):
    i += 1
    result = f'{N} * {i} = {N * i}'
    print(result) 