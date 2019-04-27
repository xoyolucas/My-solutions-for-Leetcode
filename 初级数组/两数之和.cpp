#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result;
    for(size_t i = 0; i < nums.size()-1; i++){
        for(size_t j = i+1; j < nums.size(); j++){
            if(nums[i]+nums[j]==target){
                result.push_back(i);
                result.push_back(j);
                break;
            }
        }      
    }
    return result;
}

int main(int argc, char const *argv[]){
    int tmp[5]={1,1,3,2};
    vector<int> nums1(tmp,tmp+5);
    vector<int> result=twoSum(nums1,5);
    for(size_t i = 0; i < result.size(); i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
