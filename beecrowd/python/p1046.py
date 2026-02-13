# Tempo de Jogo

start, end = map(int, input().split())
if start > end:
    duration = (24 - start) + end
elif start < end:
    duration = end - start
else:
    duration = 24
print(f'O JOGO DUROU {duration} HORA(S)')
