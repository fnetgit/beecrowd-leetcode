# Média 2

import sys

A, B, C = map(float, sys.stdin.read().split())
sys.stdout.write(f"MEDIA = {(A * 2 + B * 3 + C * 5) / 10:.1f}\n")
