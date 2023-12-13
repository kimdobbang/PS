# A, B = int(input().split()) -> 오류 원인: 리스트는 정수형int로 바꿀 수 없음 => 해결: map함수 이용
# map(적용할 함수, 반복 가능 자료형)

A, B = map(int, input().split())

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)