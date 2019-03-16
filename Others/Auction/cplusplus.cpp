#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> getHgih(map<int,int> &m, int num){
    vector<pair<int,int>> tmp;
    for(auto &o: m){
        tmp.push_back(make_pair(o.first, o.second));
    }
    sort(tmp.begin(),tmp.end(),greater<pair<int,int>>());
    vector<int> ans;
    for(auto &p: tmp){
        if(num > 0) ans.push_back(p.first);
        else break;
        num--;
    }
    return ans;
}


int main(){

    int Ntypes, Musers, Alines;
    cin >> Ntypes >> Musers >> Alines;

    int Nitems[Ntypes+1] = {0};
    for(int i=1; i<Ntypes+1; i++){
        scanf("%d",&Nitems[i]);
    }

    //[ {1:50, 2:60} ]
    vector<map<int,int>> bagKetByType(Ntypes+1);
    for(int i=0; i<Alines; i++){
        char letter;
        int label,item,value;
        cin >> letter;
        if(letter == 'B'){
            cin >> label >> item >> value;
            bagKetByType[item][label] = value;
            cout << label << " " << item << " " << bagKetByType[item][label] << endl;
        }else{
            auto kk = bagKetByType[item].find(label);
            if(kk!= bagKetByType[item].end()) bagKetByType[item].erase(kk);
        }
    }

    vector<vector<int>> bagKetByUsers(Musers+1);
    for(int i=1; i<Ntypes+1; i++){
        vector<int> user = getHgih(bagKetByType[i], Nitems[i]);
        for(auto &la: user){
            bagKetByUsers[la].push_back(i);
        }
    }

    for(int i=1; i<Musers+1; i++){
        if(bagKetByUsers[i].empty()){
            cout << "NONE\n";
        }else{
            for(auto &k: bagKetByUsers[i]){
                cout << k << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}
