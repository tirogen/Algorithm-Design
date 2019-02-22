#include <iostream>
using namespace std;
int main(){
    int n,w,M;
    cin >> n >> w;
    int L[n];
    for(int i=0; i<n; i++){
        scanf("%d", &L[i]);
    }
    M = L[0];
    for(int i=0; i<n; i++){
        int zum = 0;
        for(int k=0; k<w; k++){
            if(i+k<n) zum += L[i+k];
            M = max(M, zum);
            if(zum < 0){
                i = i + k;
                break;
            }
        }
    }
    cout << M;
    return 0;
}