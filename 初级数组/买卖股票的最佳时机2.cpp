#include <iostream>
#include <vector>
using namespace std;

int maxProfit(vector<int>& prices) {
    int maxProfit=0;
    for(size_t i = 1; i < prices.size(); i++){
        if(prices[i]-prices[i-1]>0)
            maxProfit+=prices[i]-prices[i-1];
    }
    return maxProfit;
};

int main(int argc, char const *argv[]){
    int tmp[6]={7,1,5,3,6,4};
    vector<int> nums(tmp,tmp+6);
    cout<<maxProfit(nums)<<endl;
    return 0;
}