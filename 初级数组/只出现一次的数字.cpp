#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int singleNumber(vector<int>& nums) {
    int result=nums[0];
    for(size_t i = 1; i < nums.size(); i++){
        result=result^nums[i];
    }
    return result;
}

int main(int argc, char const *argv[]){
    int tmp[5]={1,1,2,4,2};
    vector<int> nums(tmp,tmp+5);
    cout<<singleNumber(nums)<<endl;
    return 0;
}