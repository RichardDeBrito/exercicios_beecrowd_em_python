values = input().split()
x, y = float(values[0]), float(values[1])

if x > 0 and y > 0: 
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x != 0 and y == 0:
    print('Eixo X')
elif x == 0 and y == 0:
    print('Origem')