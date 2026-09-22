# Conversão de Tempo

import sys

n = int(sys.stdin.read())
sys.stdout.write(f"{n // 3600}:{n % 3600 // 60}:{n % 60}\n")
