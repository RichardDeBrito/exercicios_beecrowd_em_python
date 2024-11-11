cases = int(input())
list_odds = []
list_sums = []
sum = 0

for _ in range(0, cases):
    values = input().split()
    v1, v2 = int(values[0]), int(values[1])
    for _ in range(min(v1, v2) + 1, max(v1,v2)):
        if _ % 2 != 0:
            list_odds.append(_)
    
    
    for odd in list_odds:
        sum += odd
    
    list_sums.append(sum)
    list_odds = []
    sum = 0

for result in list_sums:
    print(result)