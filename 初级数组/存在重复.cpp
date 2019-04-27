#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(),nums.end());

    for(size_t i = 1; i < nums.size(); i++){
        if(nums[i]==nums[i-1])
            return true;
    }
    return false;
}

int main(int argc, char const *argv[]){
    int tmp[6]={7,1,5,3,1,4};
    vector<int> nums(tmp,tmp+6);
    cout<<containsDuplicate(nums)<<endl;
    return 0;
}