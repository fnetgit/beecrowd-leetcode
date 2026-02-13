# Notas e Moedas

while True:
    value = float(input())
    value = int(value * 100)  # Converte para centavos
    print('NOTAS:')
    brl_100_bill = value // 10000
    remainder = value % 10000
    print(f'{brl_100_bill:.0f} nota(s) de R$ 100.00')

    brl_50_bill = remainder // 5000
    remainder %= 5000
    print(f'{brl_50_bill:.0f} nota(s) de R$ 50.00')

    brl_20_bill = remainder // 2000
    remainder %= 2000
    print(f'{brl_20_bill:.0f} nota(s) de R$ 20.00')

    brl_10_bill = remainder // 1000
    remainder %= 1000
    print(f'{brl_10_bill:.0f} nota(s) de R$ 10.00')

    brl_5_bill = remainder // 500
    remainder %= 500
    print(f'{brl_5_bill:.0f} nota(s) de R$ 5.00')

    brl_2_bill = remainder // 200
    remainder %= 200
    print(f'{brl_2_bill:.0f} nota(s) de R$ 2.00')

    print('MOEDAS:')
    brl_1_coin = remainder // 100
    remainder %= 100
    print(f'{brl_1_coin:.0f} moeda(s) de R$ 1.00')

    brl_50_coin = remainder // 50
    remainder %= 50
    print(f'{brl_50_coin:.0f} moeda(s) de R$ 0.50')

    brl_25_coin = remainder // 25
    remainder %= 25
    print(f'{brl_25_coin:.0f} moeda(s) de R$ 0.25')

    brl_10_coin = remainder // 10
    remainder %= 10
    print(f'{brl_10_coin:.0f} moeda(s) de R$ 0.10')

    brl_5_coin = remainder // 5
    remainder %= 5
    print(f'{brl_5_coin:.0f} moeda(s) de R$ 0.05')

    brl_1_coin = remainder // 1
    remainder %= 1
    print(f'{brl_1_coin:.0f} moeda(s) de R$ 0.01')
    break
