#include <iostream>
using namespace std;
int n,S[105],M[105][105];

int mcm(int i, int j){
    if(i==j) return 0;
    if(M[i][j]!=0) return M[i][j];
    int miN = float('inf');
    for(int k=i; k<j; k++){
        miN = min(miN, S[i-1]*S[k]*S[j] + mcm(i,k) + mcm(k+1,j));
    }
    return M[i][j] = miN;
}

int main(){
    cin >> n;
    for(int i=0; i<n+1; i++){
        scanf("%d",&S[i]);
    }
    cout << mcm(1,n);
    return 0;
}
