values = input().split()
v1 = int(values[0])
v2 = int(values[1])
v3 = int(values[2])

list_values = [v1, v2, v3]
noordered = [v1, v2, v3]
list_values.sort()

for c in range(0, 3):
    print(list_values[c])
    
print()
    
for c2 in range(0, 3):
    print(noordered[c2])
    