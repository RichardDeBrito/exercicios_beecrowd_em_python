numbercases = int(input())
list_values = []

for _ in range(0, numbercases):
    values = int(input())
    list_values.append(values)

out = ''

for value in list_values:
    if value == 0:
        out = 'NULL'
    else:
        if value % 2 == 0:
            out += 'EVEN '
        else:
            out += 'ODD '

        if value < 0:
            out += 'NEGATIVE'
        else:
            out += 'POSITIVE'
        
    print(out)
    out = ''
