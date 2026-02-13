# Tabuada

multiplier = 0
result = 0
multiplicand = int(input())  # fixo
if 2 < multiplicand < 1000:
    while multiplier < 10:
        multiplier += 1
        result = multiplier * multiplicand
        print(f'{multiplier} x {multiplicand} = {result}')
