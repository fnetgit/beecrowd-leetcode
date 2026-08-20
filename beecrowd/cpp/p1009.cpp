#include <bits/stdc++.h>

using namespace std;

int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string n;
    double s, v;

    cin >> n >> s >> v;
    cout << fixed << setprecision(2) << "TOTAL = R$ " << s + v * 0.15 << '\n';

    return 0;
}
