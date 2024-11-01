abc = input().split()
a,b,c = int(abc[0]), int(abc[1]), int(abc[2])

maiorab = (a + b + abs(a-b))/2
maiorabc = int((maiorab + c + abs(maiorab - c))/2)

print(f'{maiorabc} eh o maior')
