#include <iostream>
using namespace std;

int main(){
    int a,n;
    cin >> a >> n;
    int A[a];
    for(int i=0; i<a; i++) scanf("%d", &A[i]);
    for(int i=0; i<n; i++){
        int tmp;
        bool isBreak = false;
        scanf("%d", &tmp);
        for(int i=0; i<a; i++){
            int l = i+1;
            int r = a-1;
            while(l < r){
                int zum = A[i]+A[l]+A[r];
                if(zum == tmp){
                    cout << "YES\n";
                    isBreak = true;
                    break;
                }else if(zum > tmp){
                    r--;
                }else{
                    l++;
                }
            }
            if(isBreak) break;
        }
        if(!isBreak) cout << "NO\n";
    }
    return 0;
}
