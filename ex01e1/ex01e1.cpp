#include <iostream>
#include <map>
using namespace std;

bool check(map<int, bool> &number, const int &num){
    for(auto &it: number){
        if(number[num-it.first]) return true;
        else number.erase(num-it.first);
    }
    return false;
}

int main(){
    int n,m;
    cin >> n >> m;
    map<int, bool> number;
    for(int i=0; i<n; i++){
        int store;
        cin >> store;
        number[store] = true;
    }
    for(int i=0; i<m; i++){
        int store;
        cin >> store;
        if(check(number, store)) cout << "YES";
        else cout << "NO";
        if(i!=m-1) cout << endl;
    }
    return 0;
}
