# Salário com Bônus

import sys

d = sys.stdin.read().split()
sys.stdout.write(f"TOTAL = R$ {float(d[-2]) + (float(d[-1]) * 0.15):.2f}\n")
