#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<int>& nums, int k) {
    int count=0;   
    k=k%nums.size();
    for(size_t i = 0; count < nums.size(); i++){
        int index=i;
        int tmp=nums[index];
        do{
            int index2=(index+k)%nums.size();
            int tmp2=nums[index2];
            nums[index2]=tmp;
            tmp=tmp2;
            index=index2;
            count++;
        }while(index!=i); 
    }
}

int main(int argc, char const *argv[]){
    int tmp[6]={1,2,3,4,5,6};
    vector<int> nums(tmp,tmp+6);
    rotate(nums,2);
    for(size_t i = 0; i < nums.size(); i++){
        cout<<nums[i]<<" ";
    }
    
    return 0;
}