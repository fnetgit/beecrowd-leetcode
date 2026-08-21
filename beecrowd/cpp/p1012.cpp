// Área

#include <bits/stdc++.h>

using namespace std;

int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    double a, b, c;
    cin >> a >> b >> c;
    cout << fixed << setprecision(3) << "TRIANGULO: " << (a * c) / 2 << '\n'
         << "CIRCULO: " << 3.14159 * pow(c, 2) << '\n'
         << "TRAPEZIO: " << (a + b) * c / 2 << '\n'
         << "QUADRADO: " << b * b << '\n'
         << "RETANGULO: " << a * b << '\n';

    return 0;
}
