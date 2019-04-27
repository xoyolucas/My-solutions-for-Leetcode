#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int> &nums){
    if(nums.empty())
        return 0;
    int n=0;
    for (int i = 1; i < nums.size(); i++){
        if(nums[i]!=nums[n]){
            n++;
            nums[n]=nums[i];
        }
    }
    return n+1;
}

int main(int argc, char const *argv[]){
    int tmp[10]={0,0,1,1,1,2,2,3,3,4};
    vector<int> nums(tmp,tmp+10);
    cout<<removeDuplicates(nums)<<endl;
    return 0;
}