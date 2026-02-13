# Bactéria I

import sys

for line in sys.stdin:
    genetic_code = line.strip()
    letters_of_resistance = input().strip()
    if letters_of_resistance in genetic_code:
        print('Resistente')
    else:
        print('Nao resistente')
