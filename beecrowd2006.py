certo = int(input())
pess = input().split()
v1, v2, v3, v4, v5 = int(pess[0]), int(pess[1]), int(pess[2]), int(pess[3]), int(pess[4])
list_values = [v1, v2, v3, v4, v5]

quantcerto = 0

for value in list_values:
    if value == certo:
        quantcerto +=1

print(quantcerto)