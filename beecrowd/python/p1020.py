# Idade em Dias

import sys

t = int(sys.stdin.read())
sys.stdout.write(f"{t // 365} ano(s)\n{t % 365 // 30} mes(es)\n{t % 365 % 30} dia(s)\n")
