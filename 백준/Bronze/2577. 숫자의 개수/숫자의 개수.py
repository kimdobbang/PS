A = int(input())
B = int(input())
C = int(input())
number = A * B * C

# A, B, C 곱한 값 자리수 나누어 list로 변환
# number_lst = list(map(int, str(number)))
number_lst = [int(i) for i in str(number)]

# 카운트 배열 생성: 숫자가 0 ~ 9
cnt = [0] * 10

# 카운트 배열의 index에 numver_list 요소들의 빈도 할당
for i in range(len(number_lst)):
    cnt[number_lst[i]] += 1
print(*cnt, sep='\n')

'''# 복습 : 가장 빈도가 적은 수와 빈도 구하기 (단, 빈도가 같다면 가장 큰 수)
min_val = 999999999
min_idx2 = 0
for i in range(len(cnt)):
    if cnt[i] <= min_val:
        min_val = cnt[i]
        min_idx2 = i
print(f'적은수:{min_idx2} 빈도:{min_val}')

# 복습2 : (반복문 역순으로 순회)
min_val2 = 999999999
min_idx2 = 0
for i in range(len(cnt)-1, -1, -1):  # len(cnt)에 -1 안하면 IndexError
    if cnt[i] < min_val2:
        min_val2 = cnt[i]
        min_idx2 = i
print(f'적은수:{min_idx2} 빈도:{min_val2}')'''
