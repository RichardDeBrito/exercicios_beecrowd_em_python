list_pairs = []

for _ in range(0, 5):
    value = int(input())
    if value % 2 == 0:
        list_pairs.append(value)
    
print(f'{len(list_pairs)} valores pares')