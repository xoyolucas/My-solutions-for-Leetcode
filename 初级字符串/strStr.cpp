#include <iostream>
#include <string>
using namespace std;

int strStr(string haystack, string needle) {
    if(needle=="")
        return 0;
    else if(haystack.length()<needle.length())
        return -1;
    bool str=false;

    for(size_t i = 0; i < haystack.length(); i++){
        if(needle[0]==haystack[i]&&needle.length()<=haystack.length()-i){
            str=true;
            for(size_t j = 1; j < needle.length(); j++){
                if(haystack[i+j]!=needle[j])
                    str=false;
            }
        }
        if(str)
            return i;
    }
    return -1;
}

int main(int argc, char const *argv[]){
    string s1="aaaaa",s2="bba";
    cout<<strStr(s1,s2)<<endl;
    return 0;
}
