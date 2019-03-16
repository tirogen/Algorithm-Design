#include <iostream>
using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    int P[n], M[n][4*k+1];
    for(int i=0; i<n; i++){
        scanf("%d",&P[i]);
        for(int j=0; j<4*k+1; j++){
            M[i][j] = 0;
        }
    }

    for(int j=0; j<2*k+1; j++){
        if(j > k) M[n-1][j] = 0;
        else M[n-1][j] = P[n-1];
    }


    for(int i=n-2;i>-1;i--){
        for(int j=0;j<2*k+1;j++){
            if(j==0) M[i][j] = P[i] + M[i+1][2*k];
            else M[i][j] = min(P[i]+M[i+1][2*k], M[i+1][j-1]);
        }
    }
    cout << M[0][k];

    return 0;
}
