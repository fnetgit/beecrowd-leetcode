# Cédulas

import sys

m = int(sys.stdin.read())
o = [str(m)]
for n in (100, 50, 20, 10, 5, 2, 1):
    qtd, m = divmod(m, n)
    o.append(f"{qtd} nota(s) de R$ {n},00")
sys.stdout.write("\n".join(o) + "\n")
