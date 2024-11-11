list_values = []

for _ in range(0, 6):
    value = float(input())
    if value > 0:
        list_values.append(value)

sum = 0
for v in list_values:
    sum += v
    media = sum/len(list_values)

print(f'{len(list_values)} valores positivos')
print(f'{media:.1f}')