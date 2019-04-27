#include <iostream>
#include <string>
#include <limits.h>
using namespace std;

int myAtoi(string str) {
    int num=0;
    bool neg=false;
    int begin=0;
    while(str[begin]==' ')
        ++begin;
    
    for(size_t i = begin; i < str.length(); i++){
        if(i==begin&&(str[i]=='-'||str[i]=='+')){
            if(str[i]=='-')
                neg=true;
        }
        else if(str[i]>='0'&&str[i]<='9'){
            if(num<INT_MAX/10)
                num=num*10+str[i]-'0';
            else if (num == INT_MAX/10){
                if(neg)
                    return (str[i]-'0' >= 8)? INT_MIN: ((num*10 + str[i]-'0')*-1);
                else
                    return (str[i]-'0' >= 7)? INT_MAX: (num*10 + str[i]-'0');
            }
            else
                return (neg)? INT_MIN: INT_MAX;             
        }
        else
            break;
    }
    return (neg)?(-1*num):num;
}

int main(int argc, char const *argv[]){
    string s="-91283472332";
    cout<<myAtoi(s)<<endl;
    return 0;
}
