N = int(input())
C = []
R = []
S = []


for _ in range(0, N):
    inp = input().split()
    number = int(inp[0])
    typeofguineapig = inp[1]
    if typeofguineapig == 'C':
        C.append(number)
    elif typeofguineapig == 'R':
        R.append(number)
    elif typeofguineapig == 'S':
        S.append(number)

sumC = 0
sumR = 0
sumS = 0

for value in C:
    sumC += value
for value in R:
    sumR += value
for value in S:
    sumS += value
    
totalguineapig = sumC + sumR + sumS

percentageC = (sumC*100)/totalguineapig
percentageR = (sumR*100)/totalguineapig
percentageS = (sumS*100)/totalguineapig

print(f'Total: {totalguineapig} cobaias')
print(f'Total de coelhos: {sumC}')
print(f'Total de ratos: {sumR}')
print(f'Total de sapos: {sumS}')
print(f'Percentual de coelhos: {percentageC:.2f} %')
print(f'Percentual de ratos: {percentageR:.2f} %')
print(f'Percentual de sapos: {percentageS:.2f} %')