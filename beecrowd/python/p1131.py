# Grenais

new_grenal = 1
matches = victories_inter = victories_gremio = tie = 0

while new_grenal == 1:
    goals = (input()).split()

    inter = int(goals[0])
    gremio = int(goals[1])

    matches += 1

    if inter > gremio:
        victories_inter += 1
    elif gremio > inter:
        victories_gremio += 1
    elif inter == gremio:
        tie += 1

    new_grenal = int(input('Novo grenal (1-sim 2-nao)\n'))

    if new_grenal == 2:
        break

print(f'{matches} grenais')
print(f'Inter:{victories_inter}')
print(f'Gremio:{victories_gremio}')
print(f'Empates:{tie}')

if victories_inter > victories_gremio:
    print('Inter venceu mais')
elif victories_gremio > victories_inter:
    print('Gremio venceu mais')
