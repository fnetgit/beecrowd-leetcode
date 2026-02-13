# Tipo de Combustível

alcohol = 0
gasoline = 0
diesel = 0
while True:
    user_input = int(input())
    if user_input == 1:
        alcohol += 1
    elif user_input == 2:
        gasoline += 1
    elif user_input == 3:
        diesel += 1
    if user_input == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {alcohol}\nGasolina: {gasoline}\nDiesel: {diesel}')
        break
