// Cédulas

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    const int nts[] = {100, 50, 20, 10, 5, 2, 1};
    cout << n << '\n';
    for (int nt : nts)
    {
        cout << n / nt << " nota(s) de R$ " << nt << ",00\n";
        n %= nt;
    }

    return 0;
}
