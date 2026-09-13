# Salário

import sys

d = sys.stdin.read().split()
sys.stdout.write(f'NUMBER = {d[0]}\n'
      f'SALARY = U$ {int(d[1])*float(d[2]):.2f}\n')
