valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

areatri = (A * C)/2
areacir = 3.14159 * (C**2)
areatra = ((A + B) * C)/2
areaqua = B**2
arearet = A * B

print(f'TRIANGULO: {areatri:.3f}')
print(f'CIRCULO: {areacir:.3f}')
print(f'TRAPEZIO: {areatra:.3f}')
print(f'QUADRADO: {areaqua:.3f}')
print(f'RETANGULO: {arearet:.3f}')