X = int(input())

if X%2 == 0:
    X += 1

for _ in range(X, X+12, 2):
    print(_)