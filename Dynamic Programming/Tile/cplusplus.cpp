#include <iostream>
#include <math.h>
using namespace std;

int n,A,N[15],M[15][10005];

int tile(int i, int S){
    if(i == n && S > 0) return 10000000;
    else if(i == n && S == 0) return 0;
    else if(S < 0) return 10000000;
    if(M[i][S] != 0) return M[i][S];
    int Min = 10000000;
    for(int e = 1; e < 101; e++){
        Min = min(Min, int(pow(N[i]-e,2))+tile(i+1,S-e*e)   );
    }
    return M[i][S] = Min;

}

int main(){
    cin >> n >> A;
    for(int i = 0; i < n; i++){
        scanf("%d", &N[i]);
    }
    int ans = tile(0, A);
    cout<< (ans == 10000000 ? -1 :ans);

}
