// Conversão de Tempo

#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int s, m, h;
    cin >> s;
    h = s / 3600;
    m = s % 3600 / 60;
    s %= 60;

    cout << h << ':' << m << ':' << s << '\n';

    return 0;
}
