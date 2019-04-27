#include <iostream>
#include <string>
using namespace std;

int reverse(int x) {
    long long result=0;
    bool negative=false;
    if(x<0){
        x*=-1;
        negative=true;
    }
    while(x>0){
        result=result*10+x%10;
        if(result>=0x7fffffff){
            result=0;
            break;
        }
        x/=10;    
    }
    if(negative)
        result*=-1;
    return result;
}

int main(int argc, char const *argv[]){
    int s=1534236469;
    cout<<reverse(s)<<endl;
    return 0;
}
