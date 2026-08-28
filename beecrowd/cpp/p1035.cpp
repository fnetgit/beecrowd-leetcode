// Teste de Seleção 1

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c, d;
    cin >> a >> b >> c >> d;
    (b > c && d > a && (c + d) > (a + b) && c > 0 && d > 0 && a % 2 == 0) ? cout << "Valores aceitos\n" : cout << "Valores nao aceitos\n";

    return 0;
}