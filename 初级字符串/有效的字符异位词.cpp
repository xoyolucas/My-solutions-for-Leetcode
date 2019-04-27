#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isAnagram(string s, string t) {
    sort(s.begin(),s.end());
    sort(t.begin(),t.end());
    if(s==t)
        return true;
    else
        return false;
}

int main(int argc, char const *argv[]){
    string s1="fuck";
    cout<<isAnagram(s1,s1)<<endl;
    return 0;
}
