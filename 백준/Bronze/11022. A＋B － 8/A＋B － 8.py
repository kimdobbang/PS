t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split()) 
    # print(f'Case #{i}: {a} + {b} = {a + b}')
    print('Case #{}: {} + {} = {}'.format(i, a, b, a + b))