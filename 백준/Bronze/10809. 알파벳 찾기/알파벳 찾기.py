S = input()
result = [-1]*26

for i in range(len(S)):
    if result[ord(S[i]) - 97] == -1:
        result[ord(S[i]) - 97] = i
print(*result)

# a, b, c ,d 가 result 배열의 index가 된다는건데. 이 부분 때문에 풀기 어려움 느낌
# 알파벳 문자열의 값이 a~z 배열에 있는지 찾아야할까? OR a~z 배열의 알파벳들이 문자열에 있는지 확인해할지 이런 기준을 잘 모르겠다 ㅜㅜ
