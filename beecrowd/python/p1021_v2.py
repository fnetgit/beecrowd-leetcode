# Notas e Moedas

bills = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]

total_amount = int(float(input()) * 100)  # montante total em centavos

print('NOTAS:')
for bill in bills:
    quantity = total_amount // bill
    total_amount %= bill
    print(f'{quantity} nota(s) de R$ {bill / 100:.2f}')

print('MOEDAS:')
for coin in coins:
    quantity = total_amount // coin
    total_amount %= coin
    print(f'{quantity} moeda(s) de R$ {coin / 100:.2f}')
