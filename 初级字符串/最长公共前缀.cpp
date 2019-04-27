#include <iostream>
#include <string>
#include <vector>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 0) return "";
    for (int i = 0; i < strs[0].length() ; i++){
        char c = strs[0][i];
        for (int j = 1; j < strs.size(); j ++) {
            if (i == strs[j].length() || strs[j][i] != c)
                return strs[0].substr(0,i);             
        }
    }
    return strs[0];  
}

int main(int argc, char const *argv[]){
    string tmp[3]={"flower","flow","flight"};
    vector<string> strs(tmp,tmp+3);
    cout<<longestCommonPrefix(strs)<<endl;
    return 0;
}
