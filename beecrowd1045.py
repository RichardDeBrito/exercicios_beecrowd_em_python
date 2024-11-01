values = input().split()
v1, v2, v3 = float(values[0]), float(values[1]), float(values[2])
list_values = [v1, v2, v3]
list_values.sort(reverse=True)
A = list_values[0]
B = list_values[1]
C = list_values[2]

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
elif (A**2) == (B**2) + (C**2):
    print('TRIANGULO RETANGULO') 
elif (A**2) > (B**2) + (C**2):
    print('TRIANGULO OBTUSANGULO')
elif (A**2) < (B**2) + (C**2):
    print('TRIAGULO ACUTANGULO')
elif A == B == C:
    print('TRIANGULO EQUILATERO')
elif A == B and B == C and A == C:
    print('TRIANGULO ISOSCELES')