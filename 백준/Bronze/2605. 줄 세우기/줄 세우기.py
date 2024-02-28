N = int(input())
num = list(map(int, input().split()))  # 뽑은 번호
arr = []
for i in range(1, N+1):  # 학생 0 ~ N명
    # arr.insert(-num[i-1], i)  # 출력은 같으나 오답임 -> arr에 원소 1개일 때 오답됨. 0과 -1이 가르키는 곳은 같지만, insert하는 위치 다름
    arr.insert(len(arr)-num[i-1], i)
print(*arr)
