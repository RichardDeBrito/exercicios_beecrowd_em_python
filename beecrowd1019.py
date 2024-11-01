value = int(input())
div = value//60
if div == 0:
    Seg = div
    Seg = value%60
    print(f'0:0:{Seg}')
elif 0 < div < 60:
    Min = div
    Seg = value%60
    print(f'0:{Min}:{Seg}')
else:
    Hourmore = div
    Hour = Hourmore//60
    Min = Hourmore%60
    Seg = value%60   
    print(f'{Hour}:{Min}:{Seg}') 
    