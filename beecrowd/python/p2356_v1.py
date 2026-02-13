# Bactéria I

while True:
    try:
        genetic_code = input()
        letters_of_resistance = input()
        if letters_of_resistance in genetic_code:
            print('Resistente')
        else:
            print('Nao resistente')
    except EOFError:
        break

# Deu erro (100%), pq ele quer ler todos os casos de teste até o fim do arquivo, e eu dei só dois casos pra ele ler
""" for i in range(2):
    cod_gen = input()
    letras_resisten = input()
    if letras_resisten in cod_gen:
        print('Resistente')
    else:
        print('Nao resistente') 
"""

# Deu erro (Runtime error) pq ele tava pedindo infinito
""" while True:
        cod_gen = input()
        letras_resisten = input()
        if letras_resisten in cod_gen:
            print('Resistente')
        else:
            print('Nao resistente')
 """
