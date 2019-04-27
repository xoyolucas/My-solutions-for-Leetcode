#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void moveZeroes(vector<int>& nums) {
    vector<int>::iterator it=nums.begin();
    int n=nums.size();
    
    for(size_t i = 0; i < n; i++){
        if(*it==0){
            nums.erase(it);
            nums.insert(nums.end(),0);    
        }
        else
            it++;
    }
}

int main(int argc, char const *argv[]){
    int tmp[6]={0,0,0,3,1,0};
    vector<int> nums(tmp,tmp+6);
    moveZeroes(nums);
    for(size_t i = 0; i < nums.size(); i++){
        cout<<nums[i]<<" ";
    }
    return 0;
}