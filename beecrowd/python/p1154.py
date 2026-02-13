# Idades

total_numbers = 0
total_sum = 0

while True:
    age = int(input())
    if age < 0:
        break
    total_numbers += 1
    total_sum += age

if total_numbers > 0:
    average = total_sum / total_numbers
    print(f'{average:.2f}')
