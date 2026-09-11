# Média 1

import sys

A, B = map(float, sys.stdin.read().split())
sys.stdout.write(f"MEDIA = {(A * 3.5 + B * 7.5) / 11:.5f}\n")
