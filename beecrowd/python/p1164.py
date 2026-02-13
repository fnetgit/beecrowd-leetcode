# Número Perfeito

case_of_tests = int(input())

for _ in range(case_of_tests):
    num = int(input())

    divisors_sum = 0
    for i in range(1, num):

        if num % i == 0:
            divisors_sum += i

    if divisors_sum == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
