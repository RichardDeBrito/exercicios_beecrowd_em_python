X = int(input())
Y = int(input())

minor = min(X,Y)
bigger = max(X,Y)

list_odds = []

if minor % 2 != 0:
    minor += 1
    
for _ in range(minor + 1, bigger, 2):
    list_odds.append(_)

sum = 0

for _ in list_odds:
    sum += _
    
print(sum)