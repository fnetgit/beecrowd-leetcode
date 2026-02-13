# Conversão de Tempo

n = int(input())
hours = n // 3600
rest = n % 3600
minutes = rest // 60
seconds = rest % 60

print(f'{hours}:{minutes}:{seconds}')
