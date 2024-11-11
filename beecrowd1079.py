N = int(input())
list_result = []

for _ in range(0, N):
    values = input().split()
    v1, v2, v3 = float(values[0]), float(values[1]), float(values[2])
    
    average = ((v1 * 2) + (v2 * 3) + (v3 * 5))/ 10
    list_result.append(average)
    
for result in list_result:
    print(f'{result:.1f}')