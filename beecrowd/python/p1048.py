# Aumento de Salário

salary = float(input())

if 0 <= salary <= 400:
    new_salary = salary * 0.15 + salary
    adjustment = new_salary - salary
    percentage = "15 %"
elif 400.01 <= salary <= 800.00:
    new_salary = salary * 0.12 + salary
    adjustment = new_salary - salary
    percentage = "12 %"
elif 800.01 <= salary <= 1200.00:
    new_salary = salary * 0.10 + salary
    adjustment = new_salary - salary
    percentage = "10 %"
elif 1200.01 <= salary <= 2000.00:
    new_salary = salary * 0.07 + salary
    adjustment = new_salary - salary
    percentage = "7 %"
elif salary > 2000.00:
    new_salary = salary * 0.04 + salary
    adjustment = new_salary - salary
    percentage = "4 %"

print(f'Novo salario: {new_salary:.2f}\n'
      f'Reajuste ganho: {adjustment:.2f}\n'
      f'Em percentual: {percentage}')
