salary = float(input())

if 0.0 < salary <= 400.0:
    new_salary = salary + (salary * (15/100))
    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {salary * (15/100):.2f}')
    print(f'Em percentual: 15 %')
elif 400.0 < salary <= 800.0:
    new_salary = salary + (salary * (12/100))
    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {salary * (12/100):.2f}')
    print(f'Em percentual: 12 %')
elif 800.0 < salary <= 1200.0:
    new_salary = salary + (salary * (10/100))
    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {salary * (10/100):.2f}')
    print(f'Em percentual: 10 %')
elif 1200.0 < salary <= 2000.0:
    new_salary = salary + (salary * (7/100))
    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {salary * (7/100):.2f}')
    print(f'Em percentual: 7 %')
else:
    new_salary = salary + (salary * (4/100))
    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {salary * (4/100):.2f}')
    print(f'Em percentual: 4 %')
    