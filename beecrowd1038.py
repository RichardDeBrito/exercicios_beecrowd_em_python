input = input().split()
code = input[0]
amount = int(input[1])

list_shopping = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}

res = list_shopping[code] * amount
print(f'Total: R$ {res:.2f}')
