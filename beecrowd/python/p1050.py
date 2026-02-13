# DDD

list = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

ddd = int(input())
if ddd in list:
    # Se o código DDD estiver presente no dicionário, imprime o nome da cidade correspondente ao código DDD digitado pelo usuário.
    print(list[ddd])
else:
    print('DDD nao cadastrado')
