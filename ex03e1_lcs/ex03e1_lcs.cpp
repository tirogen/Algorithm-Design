#include <iostream>
using namespace std;

int lcs(string one, string two, int pone, int ptwo){
    if(pone == one.length() || ptwo == two.length()) return 0;
    if(one[pone] == two[ptwo]){
        cout << one[pone] << " - " << two[ptwo] << endl;
        return 1+lcs(one, two, ++pone, ++ptwo);
    }else{
        cout << pone << " x " << ptwo << endl;
        return max(lcs(one, two, ++pone, ptwo), lcs(one, two, pone, ++ptwo));
    }
}

int main(){
    string one, two;
    cin >> one >> two;
    cout << lcs(one, two, 0, 0);
}
