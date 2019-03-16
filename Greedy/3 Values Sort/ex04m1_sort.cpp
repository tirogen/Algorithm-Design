#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print(string st,const vector<int> &o){
    cout<<st<<":";
    for(auto &i: o){
        cout<<i<<" ";
    }
    cout<<endl;
}

vector<int> sort_diff(vector<int> srt){
    vector<int> diff;
    vector<int> clone(srt);
    sort(srt.begin(), srt.end());
    for(int i=0; i<srt.size(); i++){
        if(srt[i]!=clone[i]) diff.push_back(clone[i]);
    }
    return diff;
}

int main(){
    int n, coun=0;
    vector<int> num,sn_num;
    cin >> n;
    for(int i=0; i<n; i++){
        int store;
        cin >> store;
        num.push_back(store);
    }

    sn_num = sort_diff(num);

    while(sn_num.size()!=0){
        //print("sn_num start",sn_num);

        vector<int> st_num(sn_num);
        sort(st_num.begin(), st_num.end());


        if(sn_num[0]==3 && st_num[0]==1){
            auto it = find(sn_num.rbegin(),sn_num.rend(),st_num[0]);
            swap(sn_num[0],*it);
        }else if(sn_num[0]==3){
            auto it = find(sn_num.begin(),sn_num.end(),st_num[0]);
            swap(sn_num[0],*it);
        }else{
            //equal 2
            int n1 = count(st_num.begin(),st_num.end(),1);
            auto it = (find(sn_num.begin()+n1, sn_num.end(), 2)!=sn_num.end()) ? find(sn_num.begin()+n1,sn_num.end(),1) : find(sn_num.begin(),sn_num.end(),1);
            swap(sn_num[0],*it);
        }
        coun++;
       // print("sn_num after swap",sn_num);

        sn_num = sort_diff(sn_num);

        //print("sn_num before end", sn_num);
    }

    cout << coun;

    return 0;
}
