valores1 = input().split()
valores2 = input().split()

cod1 = int(valores1[0])
num1 = int(valores1[1])
uni1 = float(valores1[2])

res1 = num1 * uni1

cod2 = int(valores2[0])
num2 = int(valores2[1])
uni2 = float(valores2[2])

res2 = num2 * uni2

print(f'VALOR A PAGAR: R$ {res1 + res2:.2f}')