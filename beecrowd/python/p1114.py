# Senha Fixa

password = 2002
while True:
    attempt = int(input())
    if attempt != password:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break
