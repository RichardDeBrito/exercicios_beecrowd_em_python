I = 0
J = 1

for _ in range(0, 3):
    print(f'I={I} J={J}')
    J += 1

I = 0.2
sum = 0.2
J = 1.2

for _ in range(0,4):
    for _ in range(0,3):
        print(f'I={I:.1f} J={J:.1f}')
        J += 1
    J = 1.2
    J += sum
    sum += 0.2
    
    I += 0.2
    
I = 1
J = 2

for _ in range(0, 3):
    print(f'I={I} J={J}')
    J += 1
    
I = 1.2
J = 2.2

for _ in range(0,4):
    for _ in range(0,3):
        print(f'I={I:.1f} J={J:.1f}')
        J += 1
    J = 1.4
    J += sum
    sum += 0.2
    
    I += 0.2
    
I = 2
J = 3


for _ in range(0,3):
    print(f'I={I} J={J}')
    J += 1