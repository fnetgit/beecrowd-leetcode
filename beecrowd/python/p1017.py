# Gasto de Combustível

import sys

h, s = map(int, sys.stdin.read().split())
sys.stdout.write(f"{h * s / 12.0:.3f}\n")
