# Número Primo

def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


data_inputs = int(input())
for _ in range(data_inputs):
    number = int(input())
    if eh_primo(number):
        print(f'{number} eh primo')
    else:
        print(f'{number} nao eh primo')
