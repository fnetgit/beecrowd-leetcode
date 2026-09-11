# Diferença

import sys

A, B, C, D = map(int, sys.stdin.read().split())
sys.stdout.write(f"DIFERENCA = {(A * B) - (C * D)}\n")
