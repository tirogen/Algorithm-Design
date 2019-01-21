#include <iostream>
using namespace std;

int main(){
    int h,m,p;
    cin >> h >> m >> p;
    m += p;
    p = m/60;
    m %= 60;
    h += p;
    h %= 24;
    if(h < 10) cout << "0" << h << " ";
    else cout << h << " ";
    if (m < 10) cout << "0" << m;
    else cout << m;
    return 0;
}
