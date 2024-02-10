word = input().upper()  # 대문자로 변환
cnt = [0] * 26  # 카운트 배열 생성
# 카운트 배열에 알파벳 종류별로 갯수 count
for i in range(len(cnt)):
    for j in range(len(word)):
        if i == (ord(word[j]) - 65):
            cnt[i] += 1
# print(cnt)

# 알파벳의 최빈값
max_idx = 0
max_v = 0
for i in range(len(cnt)):
    if cnt[i] > max_v:
        max_v = cnt[i]
        max_idx = i

# 최빈값의 갯수
max_cnt = 0
for i in cnt:
    if i == max_v:
        max_cnt += 1

# 정답 출력
if max_cnt > 1:
    print('?')
elif max_cnt == 1:
    print(chr(max_idx + 65))