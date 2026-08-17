// Área do Círculo

#include <bits/stdc++.h>

using namespace std;

int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    double r;
    cin >> r;
    cout << fixed << setprecision(4) << "A=" << 3.14159 * (r * r) << "\n";

    return 0;
}

// fixed: exibe o número em formato decimal, sem notação científica.
// setprecision(4): define 4 casas decimais depois da vírgula.