#include <iostream>
using namespace std;

int mem[500][500];

int lcs(string one, string two, int i1, int i2){
    for(int i=1; i<=i1; i++){
        for(int j=1; j<=i2; j++){
            if(one[i]==two[j]) mem[i][j] = 1+mem[i-1][j-1];
            else mem[i][j] = max(mem[i-1][j], mem[i][j-1]);
        }
    }
    return mem[one.length()][two.length()];
}

int main(){
    string one, two;
    cin >> one >> two;
    cout << lcs(one, two, one.length(), two.length());
}
