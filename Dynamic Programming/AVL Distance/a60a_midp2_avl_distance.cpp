#include <iostream>
#include <vector>
using namespace std;

int getNum(int i, int d, vector<vector<int>> &edge){
    if(i == 0) return 0;
    if(edge[i].empty() && d > 0) return 0;
    if(d == 0) return 1;
    int zum = 0;
    for(int k=0; k<edge[i].size(); k++){
        zum += getNum(edge[i][k], d-1, edge);
    }
    return zum;
}

int avl(int i, int d, vector<vector<int>> &edge){
    int left,right;
    if(edge[i].size()==2){
        left = edge[i][0];
        right =edge[i][1];
    }else if(edge[i].size()==1){
        left = edge[i][0];
        right = 0;
    }else{
        left = 0;
        right = 0;
    }
    int zum = getNum(left, d-1, edge) + getNum(right, d-1, edge);
    for(int k=0; k<d-1; k++){
        zum += getNum(left, k, edge)*getNum(right, d-2-k, edge);
    }
    return zum;
}

int main(){
    int n,k;
    cin >> n >> k;
    vector<vector<int>> edge(n+1);
    for(int i=0; i<n-1; i++){
        int a,b;
        cin >> a >> b;
        edge[a].push_back(b);
    }
    int zum = 0;
    for(int i=1; i<=n; i++){
        zum += avl(i,k,edge);
    }
    cout << zum;
    return 0;
}
