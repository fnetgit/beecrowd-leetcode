# Triângulo

a, b, c = map(float, input().split())
if a + b > c and b + c > a and c + a > b:
    perimeter = a + b + c
    print(f'Perimetro = {perimeter:.1f}')
else:
    trapezoid_area = 0.5 * (a + b) * c
    print(f'Area = {trapezoid_area:.1f}')
