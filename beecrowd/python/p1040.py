# Média 3

numbers = input().split()
n1 = float(numbers[0])
n2 = float(numbers[1])
n3 = float(numbers[2])
n4 = float(numbers[3])

average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f'Media: {average:.1f}')
if average >= 7.0:
    print('Aluno aprovado.')
    exit()

elif average < 5.0:
    print('Aluno reprovado.')
    exit()

else:
    print('Aluno em exame.')
    exam = float(input(''))
    final_average = (exam + average) / 2
    print(f'Nota do exame: {exam:.1f}')
if final_average >= 5.0:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')
print(f'Media final: {final_average:.1f}')
