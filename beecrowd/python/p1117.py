# Validação de Nota

valid_grades = []
while len(valid_grades) < 2:
    grade = float(input())
    if 0 <= grade <= 10:
        valid_grades.append(grade)
    else:
        print('nota invalida')

average = sum(valid_grades) / len(valid_grades)
print(f'media = {average:.2f}')
