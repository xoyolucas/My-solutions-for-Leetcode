#include <vector>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max=0;
        int localMax=0;
        for(int i=1;i<prices.size();++i){
            if(localMax<0)
                localMax=0;
            int tmp=prices[i]-prices[i-1];
            if(localMax>=0)
                localMax+=tmp;
            if(localMax>max)
                max=localMax;
        }
        return max;
    }
};