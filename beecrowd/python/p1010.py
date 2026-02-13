# Cálculo Simples

values1 = input().split()

code1 = int(values1[0])
quantity1 = int(values1[1])
price1 = float(values1[2])

values2 = input().split()

code2 = int(values2[0])
quantity2 = int(values2[1])
price2 = float(values2[2])

total = (quantity1 * price1) + (quantity2 * price2)
print(f'VALOR A PAGAR: R$ {total:.2f}')
