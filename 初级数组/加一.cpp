#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <map>
using namespace std;

vector<int> plusOne(vector<int>& digits) {
    vector<int> result(digits);
    vector<int>::iterator it=result.end()-1;
    bool carry=false;
    if(*it==9){
        *it=0;
        carry=true;
    }
    else
        *it+=1;
    it--;

    while(it >= result.begin()){
        if(carry&&*it==9){
            *it=0;
            it--;
            carry=true;
        }
        else if(carry){
            *it+=1;
            carry=false;
            break;
        }
        else
            break;
    }
    if(carry){
        it=result.begin();
        result.insert(it,1);
    }
    return result;
}

int main(int argc, char const *argv[]){
    int tmp[5]={1,1,3,3,2};
    vector<int> nums1(tmp,tmp+5);
    int tmp2[5]={9,9,9,9,9};
    vector<int> nums2(tmp2,tmp2+5);
    vector<int> result=plusOne(nums2);
    for(size_t i = 0; i < result.size(); i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
