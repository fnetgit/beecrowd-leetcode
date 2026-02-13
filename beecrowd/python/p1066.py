# Pares, Ímpares, Positivos e Negativos

even = 0  # contadores
odd = 0
negatives = 0
positives = 0
for i in range(5):
    number = int(input())
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{positives} valor(es) positivo(s)')
print(f'{negatives} valor(es) negativo(s)')
