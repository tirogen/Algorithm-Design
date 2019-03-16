#include <iostream>

using namespace std;

int main(){
    int n,w;
    cin >> n >> w;
    int L[n];
    for(int i=0; i<n; i++){
        scanf("%d", &L[i]);
    }

    int M = L[0];

    int i = 0;
    while(i<n){
        int zum = 0;
        for(int k=0; k<w; k++){
            if(i+k<n){
                zum = zum + L[i+k];
            }
            M = max(M, zum);
            if(zum < 0){
                i = i + k;
                break;
            }
        }
        i += 1;
    }
    cout << M;
    return 0;
}
