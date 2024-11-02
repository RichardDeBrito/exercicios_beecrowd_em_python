list_values = []
for _ in range(0, 6):
    value = float(input())
    if value > 0:
        list_values.append(value)

print(f'{len(list_values)} valores positivos')
    