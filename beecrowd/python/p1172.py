# Substituição em Vetor I

numbers = []
for i in range(10):
    user_number = int(input())
    if user_number <= 1:
        user_number = 1
    numbers.append(user_number)

for index, number in enumerate(numbers):
    print(f'X[{index}] = {number}')
