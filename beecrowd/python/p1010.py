# Cálculo Simples
import sys

t = 0
for _ in range(2):
    e = sys.stdin.readline().split()
    t += int(e[1]) * float(e[2])
print(f"VALOR A PAGAR: R$ {t:.2f}")
