# Consumo

import sys

d = sys.stdin.read().split()
sys.stdout.write(f"{int(d[0]) / float(d[1]):.3f} km/l\n")
