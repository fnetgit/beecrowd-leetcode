# Cédulas

total_money = int(input())
rest = total_money

bill100 = rest // 100
rest = rest % 100  # Resto é igual ao que sobra ao dividir resto por 100

bill50 = rest // 50
rest %= 50

bill20 = rest // 20
rest %= 20

bill10 = rest // 10
rest %= 10

bill5 = rest // 5
rest %= 5

bill2 = rest // 2
rest %= 2

bill1 = rest // 1
rest %= 1

print(f"{total_money}")
print(f"{bill100} nota(s) de R$ 100,00")
print(f"{bill50} nota(s) de R$ 50,00")
print(f"{bill20} nota(s) de R$ 20,00")
print(f"{bill10} nota(s) de R$ 10,00")
print(f"{bill5} nota(s) de R$ 5,00")
print(f"{bill2} nota(s) de R$ 2,00")
print(f"{bill1} nota(s) de R$ 1,00")
