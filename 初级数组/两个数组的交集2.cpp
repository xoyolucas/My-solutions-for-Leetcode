#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result;
    map<int,int> record;
    
    for(size_t i = 0; i < nums1.size(); i++){
        record[nums1[i]]++;
    }
    
    for(size_t i = 0; i < nums2.size(); i++){
        if(record[nums2[i]]!=0){
            result.push_back(nums2[i]);
            record[nums2[i]]--;
        }
    }
    return result;   
}

int main(int argc, char const *argv[]){
    int tmp[5]={1,1,3,3,2};
    vector<int> nums1(tmp,tmp+5);
    int tmp2[5]={1,1,2,3,3};
    vector<int> nums2(tmp2,tmp2+5);
    vector<int> result=intersect(nums1,nums2);
    for(size_t i = 0; i < result.size(); i++){
        cout<<result[i]<<" ";
    }
    return 0;
}
