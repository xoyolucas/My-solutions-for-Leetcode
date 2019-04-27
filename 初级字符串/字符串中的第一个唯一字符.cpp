#include <iostream>
#include <string>
using namespace std;

int firstUniqChar(string s) {
    for(size_t i = 0; i < s.length(); i++){
        bool single=true;
        for(size_t j = 0; j < s.length(); j++){
            if(i!=j&&s[i]==s[j]){
                single=false;
                break;
            }
        }
        if(single)
            return i;
    }
    return -1;
}

int main(int argc, char const *argv[]){
    string s="fuuck";
    cout<<firstUniqChar(s)<<endl;
    return 0;
}
