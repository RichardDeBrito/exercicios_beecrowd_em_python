value = int(input())
list_notes = [100, 50, 20, 10, 5, 2, 1]
print(value)
for note in list_notes:
    quant = value//note
    value = value%note

    print(f'{quant} nota(s) de R$ {note},00')