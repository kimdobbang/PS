
N = int(input())

out = False  # 특정 조건 일 때 바깥 for문까지 종료하도록 함
for i in range(N // 3 + 1):
    for j in range(N // 5 + 1):
        num = 3*i + 5*j
        if num == N:
            print(i + j)
            out = True  # 답 찾으면 true가 되면서 바깥 for문 종료
            break
    if (out):
        break
if (not out):  # 답 못잦고 반복문 끝까지 순회 종료하면 -1 출력
    print(-1)