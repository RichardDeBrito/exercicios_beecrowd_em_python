salary = float(input())

if 0.00 < salary <= 2000.00:
    print('Isento')
elif 2000.00 < salary <= 3000.00:
    #8% de imposto
    tax = (salary - 2000.00) * 0.08
    print(f'R$ {tax:.2f}')
    
elif 3000.00 < salary <= 4500.00:
    #18% de imposto
    tax = (salary - 3000.00) * 0.18 + (1000 * 0.08)
    print(f'R$ {tax:.2f}')
    
else:
    #28% de imposto
    tax = (salary - 4500.00) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f'R$ {tax:.2f}')