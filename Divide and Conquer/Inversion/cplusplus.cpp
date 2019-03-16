#include <iostream>
using namespace std;
int n,A[100005];
int main(){
    cin >> n;
    for(int i=0; i<n; i++){
        scanf("%d",&A[i]);
    }
    int count = 0;
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(A[i]>A[j]) count++;
        }
    }
    cout << count;
    return 0;
}