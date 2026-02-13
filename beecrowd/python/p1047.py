# Tempo de Jogo com Minutos

start_hour, start_minute, end_hour, end_minute = map(int, input().split())

start_total_minutes = start_hour * 60 + start_minute
end_total_minutes = end_hour * 60 + end_minute

if end_total_minutes >= start_total_minutes:
    total_duration = end_total_minutes - start_total_minutes
else:
    total_duration = (24 * 60 - start_total_minutes) + end_total_minutes

if total_duration == 0:
    total_duration = 1440

duration_hours = total_duration // 60
duration_minutes = total_duration % 60

print(f'O JOGO DUROU {duration_hours} HORA(S) E {duration_minutes} MINUTO(S)')
