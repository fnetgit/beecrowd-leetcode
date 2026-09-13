# Área

import sys

A, B, C = map(float, sys.stdin.read().split())

sys.stdout.write(
    f"TRIANGULO: {(A * C) / 2.0:.3f}\n"
    f"CIRCULO: {3.14159 * C * C:.3f}\n"
    f"TRAPEZIO: {(A + B) * C / 2.0:.3f}\n"
    f"QUADRADO: {B * B:.3f}\n"
    f"RETANGULO: {A * B:.3f}\n"
)
