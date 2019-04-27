class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    	if(nums.size()==0)
    		return 0;
        int local_max=nums[0],max=nums[0];
        for(int i=1;i<nums.size();++i){
        	local_max=local_max+nums[i]>nums[i]?local_max+nums[i]:nums[i];
        	max=local_max>max?local_max:max;
        }
        return max;
    }
};