# Lanche

foods = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}

values = input().split()
code = int(values[0])
quantity = int(values[1])

total = foods[code] * quantity
print(f'Total: R$ {total:.2f}')
