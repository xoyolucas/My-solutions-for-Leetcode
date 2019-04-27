class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int p1=0,p2=nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int tmp=p2;
            p2=p1+nums[i]>p2?(p1+nums[i]):p2;
            p1=tmp;
        }
        return p2;
    }
};