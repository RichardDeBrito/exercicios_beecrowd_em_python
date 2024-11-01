p1, p2 = input().split(), input().split()

x1,y1 = float(p1[0]), float(p1[1])
x2,y2 = float(p2[0]), float(p2[1])

dis = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

print(f'{dis:.4f}')