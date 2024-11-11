list_values = []

for _ in range(0, 100):
    value = int(input())
    list_values.append(value)

value_max = max(list_values)

print(value_max)
print(list_values.index(value_max) + 1)
