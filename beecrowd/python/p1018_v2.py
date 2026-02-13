# Cédulas

total_money = int(input())
rest = total_money

banknotes = [100, 50, 20, 10, 5, 2, 1]
amount_of_banknotes = []  # Lista vazia para armazenar a quantidade de cada nota

for banknote in banknotes:
    amount_of_banknotes.append(rest // banknote)
    rest %= banknote

print(total_money)
for i in range(len(banknotes)):
    print(f"{amount_of_banknotes[i]} nota(s) de R$ {banknotes[i]},00")
