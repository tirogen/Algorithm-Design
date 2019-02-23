#include <iostream>
using namespace std;
int n,h,L[1001][1001], M[1001][1001];

int diagsum(int r, int c){
    if(r==n-1 || c==n-1) return L[r][c];
    if(M[r][c]!=0) return M[r][c];
    return M[r][c] = max(L[r][c]+diagsum(r+1,c+1), L[r][c]);
}

int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            scanf("%d",&L[i][j]);
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            h = max(h, diagsum(i,j));
        }
    }
    cout << h;

    return 0;
}
