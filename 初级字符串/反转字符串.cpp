#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    int n=s.length();
    string result;
    for(size_t i = 0; i < n; i++){
        result+=s[n-1-i];        
    }
    return result;
}

int main(int argc, char const *argv[]){
    string s="fuck";
    cout<<reverseString(s)<<endl;
    return 0;
}
