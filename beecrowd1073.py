N = int(input())

if (N % 2) == 0:
    for _ in range(2, N+1, 2):
        print(f'{_}^2 = {_*_}')
else:
    for _ in range(2, N, 2):
        print(f'{_}^2 = {_*_}')
