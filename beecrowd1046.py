values = input().split()
v1, v2 = int(values[0]), int(values[1])

if v1 > v2:
    hours = (v1 - v2) - 24
    print(f'O JOGO DUROU {abs(hours)} HORA(S)')
elif v1 == v2:
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    hours2 = (v1 - v2)
    print(f'O JOGO DUROU {abs(hours2)} HORA(S)')