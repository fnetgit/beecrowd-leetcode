# Cachorros-Quentes

values = (input()).split()
total_eaten = int(values[0])
total_participants = int(values[1])
hot_dogs_per_participants = total_eaten / total_participants

print(f'{hot_dogs_per_participants:.2f}')
