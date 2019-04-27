#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isPalindrome(string s) {
    for (int i = 0, j = s.size() - 1; i < j; i++, j--) { 
        while (isalnum(s[i]) == false && i < j) i++; 
        while (isalnum(s[j]) == false && i < j) j--; 
        if (tolower(s[i]) != tolower(s[j])) return false; 
    }
    
    return true; 
}

int main(int argc, char const *argv[]){
    string s="meem";
    cout<<isPalindrome(s)<<endl;
    return 0;
}
