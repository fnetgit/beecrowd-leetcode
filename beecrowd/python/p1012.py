# Área

values = input().split()
A = float(values[0])
B = float(values[1])
C = float(values[2])

pi = 3.14159
triangle_area = (A * C)/2
circle_area = pi * C**2
trapezoid_area = (A + B) * C / 2
square_area = B**2
rectangle_area = A * B

print(f'TRIANGULO: {triangle_area:.3f}')
print(f'CIRCULO: {circle_area:.3f}')
print(f'TRAPEZIO: {trapezoid_area:.3f}')
print(f'QUADRADO: {square_area:.3f}')
print(f'RETANGULO: {rectangle_area:.3f}')
