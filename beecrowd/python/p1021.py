# Notas e Moedas

import sys

cents = int(float(sys.stdin.read()) * 100 + 0.5)

n100, cents = divmod(cents, 10000)
n50, cents = divmod(cents, 5000)
n20, cents = divmod(cents, 2000)
n10, cents = divmod(cents, 1000)
n5, cents = divmod(cents, 500)
n2, cents = divmod(cents, 200)

m1, cents = divmod(cents, 100)
m50, cents = divmod(cents, 50)
m25, cents = divmod(cents, 25)
m10, cents = divmod(cents, 10)
m5, cents = divmod(cents, 5)

sys.stdout.write(
    f"NOTAS:\n"
    f"{n100} nota(s) de R$ 100.00\n"
    f"{n50} nota(s) de R$ 50.00\n"
    f"{n20} nota(s) de R$ 20.00\n"
    f"{n10} nota(s) de R$ 10.00\n"
    f"{n5} nota(s) de R$ 5.00\n"
    f"{n2} nota(s) de R$ 2.00\n"
    f"MOEDAS:\n"
    f"{m1} moeda(s) de R$ 1.00\n"
    f"{m50} moeda(s) de R$ 0.50\n"
    f"{m25} moeda(s) de R$ 0.25\n"
    f"{m10} moeda(s) de R$ 0.10\n"
    f"{m5} moeda(s) de R$ 0.05\n"
    f"{cents} moeda(s) de R$ 0.01\n"
)
