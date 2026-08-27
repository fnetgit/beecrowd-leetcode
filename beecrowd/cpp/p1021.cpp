// Notas e Moedas

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    double t;
    int cents;
    int nts[] = {10000, 5000, 2000, 1000, 500, 200};
    int mds[] = {100, 50, 25, 10, 5, 1};
    cin >> t;
    cents = round(t * 100);
    cout << "NOTAS:\n";
    for (int nt : nts)
    {
        cout << cents / nt << " nota(s) de R$ " << nt / 100 << ".00\n";
        cents = cents % nt;
    }

    cout << "MOEDAS:\n";
    for (int md : mds)
    {
        cout << cents / md << fixed << setprecision(2) << " moeda(s) de R$ " << md / 100.00 << '\n';
        cents = cents % md;
    }
    return 0;
}