# Gasto de Combustível

hours = int(input())
average_speed = int(input())
distance_traveled = hours * average_speed
liters_consumed = distance_traveled / 12
print(f'{liters_consumed:.3f}')
