/*
 * @lc app=leetcode.cn id=47 lang=cpp
 *
 * [47] 全排列 II
 *
 * https://leetcode-cn.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (57.95%)
 * Likes:    258
 * Dislikes: 0
 * Total Accepted:    49.5K
 * Total Submissions: 85.5K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个可包含重复数字的序列，返回所有不重复的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,1,2]
 * 输出:
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 * 
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> permuteUnique(vector<int> &nums)
    {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());
        backTrack(nums, res, nums.size(), 0);
        return res;
    }

    void backTrack(vector<int> nums, vector<vector<int>> &res, int size, int index)
    {
        if (index == size - 1)
        {
            res.push_back(nums);
        }
        for (int index2 = index; index2 < size; ++index2)
        {
            // 若为重复元素则不进行递归搜索
            if (index2 != index && nums[index2] == nums[index])
            {
                continue;
            }
            swap(nums[index], nums[index2]);
            backTrack(nums, res, size, index + 1);
        }
    }
};
// @lc code=end
