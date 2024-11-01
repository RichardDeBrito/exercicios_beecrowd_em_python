values = input().split()
A, B = int(values[0]), int(values[1])

if (A%B) == 0 or (B%A) == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')