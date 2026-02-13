# Notas da prova

number_note = int(input())
if number_note == 0:
    print('E')
elif number_note in range(1, 36):
    print('D')
elif number_note in range(36, 61):
    print('C')
elif number_note in range(61, 86):
    print('B')
elif number_note in range(86, 101):
    print('A')
