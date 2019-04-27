#include <iostream>
#include <string>
using namespace std;

string countAndSay(int n) {
    if(n<=0)
        return "";
    string str="1";
    
    for(size_t i = 1; i < n; i++){
        string tmp="";
        for(size_t j = 0; j < str.length(); j++){
            int count=1;
            while((j+1)<str.length()&&str[j]==str[j+1]){
                count++;
                j++;
            }
            tmp+=to_string(count);
            tmp+=str[j];
        }
        str=tmp;
    }
    return str;
}

int main(int argc, char const *argv[]){
    int n=5;
    cout<<countAndSay(n)<<endl;
    return 0;
}
