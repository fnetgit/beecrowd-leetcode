# Distância Entre Dois Pontos

import sys
from math import sqrt

x1, y1, x2, y2 = map(float, sys.stdin.read().split())
dx = x2 - x1
dy = y2 - y1
sys.stdout.write(f"{sqrt(dx * dx + dy * dy):.4f}\n")
