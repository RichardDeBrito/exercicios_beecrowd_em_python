entrada = input().split()
hourandmin = {
    'hours1': int(entrada[0]), 
    'minutes1': int(entrada[1]), 
    'hours2': int(entrada[2]), 
    'minutes2': int(entrada[3])}

total1 = hourandmin['hours1'] * 60 + hourandmin['minutes1']
total2 = hourandmin['hours2'] * 60 + hourandmin['minutes2']

if total2 <= total1:
    total2 += 1440
    
rest = total2 - total1

hours = rest // 60
minutes = rest % 60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')