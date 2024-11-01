age = int(input())
list_div = [365, 30, 1]

for div in list_div:
    quant = age//div 
    age = age%div
    if div == 365:
        print(f'{quant} ano(s)')
    elif div == 30:
        print(f'{quant} mes(es)')
    elif div == 1:
        print(f'{quant} dia(s)')