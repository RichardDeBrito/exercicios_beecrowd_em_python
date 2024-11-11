N = int(input())
list_values = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

numberin = 0
numberout = 0

for _ in range(0, N):
    value = int(input())
    
    if value in list_values:
        numberin += 1
    else:
        numberout += 1
    
print(f'{numberin} in')
print(f'{numberout} out')