class Solution {
public:
    Solution(vector<int>& nums) {
        ori=nums;
        random=nums;
        size=ori.size();
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return ori;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for(int i=0;i<ori.size();++i){
            int j = (rand() % (size - i)) + i;
            swap(random[i], random[j]);
        }
        return random;
    }

private:
    vector<int> ori;
    vector<int> random;
    int size;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */