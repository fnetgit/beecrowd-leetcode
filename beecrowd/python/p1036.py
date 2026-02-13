# Fórmula de Bhaskara

# delta = b**2 - 4 * a * c
# Bhaskara: x = (-b +- delta** 0.5) / (2 * a)

# Se Δ > 0: Duas raízes reais e distintas.
# Se Δ = 0: Uma raiz real.
# Se Δ < 0: Duas raízes complexas.

user_input = input('')
a, b, c = map(float, user_input.split())
if a == 0:
    print('Impossivel calcular')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Impossivel calcular')
    elif delta > 0:
        r1 = (-b + delta ** 0.5) / (2 * a)
        r2 = (-b - delta ** 0.5) / (2 * a)
        print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
    else:
        r = -b / (2 * a)
        print(f'R = {r:.5f}')
