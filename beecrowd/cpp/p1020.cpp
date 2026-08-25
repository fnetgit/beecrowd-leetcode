// Idade em Dias

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int d, m, y;
    cin >> d;
    y = d / 365;
    m = d % 365 / 30;
    d = d % 365 % 30;

    cout << y << " ano(s)\n" << m << " mes(es)\n" << d << " dia(s)\n";

    return 0;
}