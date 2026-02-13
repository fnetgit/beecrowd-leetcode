# Distância Entre Dois Pontos

p1 = (input()).split()
p2 = (input()).split()
x1, y1 = map(float, p1)
x2, y2 = map(float, p2)

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f'{distance:.4f}')
