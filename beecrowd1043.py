values = input().split()
A, B, C = float(values[0]), float(values[1]), float(values[2])
if (A + B) > C and (C + B) > A and (C + A) > B:
    print(f'Perimetro = {A + B + C:.1f}')
else:
    area = ((A + B) * C)/ 2
    print(f'Area = {area:.1f}') 