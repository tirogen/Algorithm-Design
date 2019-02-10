#include <iostream>
using namespace std;

int mem[501][501];

int lcs(string one, string two, int pone, int ptwo){
    if(pone == one.length() || ptwo == two.length()) return 0;
    if(mem[pone][ptwo]!=-1) return mem[pone][ptwo];
    if(one[pone] == two[ptwo]){
        return mem[pone][ptwo] = 1+lcs(one, two, pone+1, ptwo+1);
    }else{
        return mem[pone][ptwo] = max(lcs(one, two, pone+1, ptwo), lcs(one, two, pone, ptwo+1));
    }
}

int main(){
    for(int i=0; i<501; i++){
        for(int j=0; j<501; j++){
            mem[i][j]=-1;
        }
    }

    string one, two;
    cin >> one >> two;
    cout << lcs(one, two, 0, 0);
}

