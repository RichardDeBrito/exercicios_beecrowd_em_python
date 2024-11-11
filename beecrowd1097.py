I = 1
J = 7
mult = 2

for _ in range(0, 5):
    for _ in range(0, 3):
        print(f'I={I} J={J}')
        J -= 1
    J = 7 + mult
    mult += 2
    I += 2