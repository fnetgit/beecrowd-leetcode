# Positivos e Média

positives = []
for _ in range(6):
    value = float(input())
    if value > 0:
        positives.append(value)

average = sum(positives) / len(positives)
print(f'{len(positives)} valores positivos')
print(f'{average:.1f}')
