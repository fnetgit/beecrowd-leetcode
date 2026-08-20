// Cálculo Simples

#include <bits/stdc++.h>

using namespace std;

int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    double s = 0;

    for (int i = 0; i < 2; i++)
    {
        int c, n;
        double p;
        cin >> c >> n >> p;
        s += n * p;
    }
    cout << fixed << setprecision(2) << "VALOR A PAGAR: R$ " << s << '\n';

    return 0;
}
