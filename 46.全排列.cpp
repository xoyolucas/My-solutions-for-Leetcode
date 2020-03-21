/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (74.17%)
 * Likes:    571
 * Dislikes: 0
 * Total Accepted:    91.3K
 * Total Submissions: 122.6K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,2,3]
 * 输出:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> res;
        backTrack(nums, res, nums.size(), 0);
        return res;
    }

    void backTrack(vector<int> &nums, vector<vector<int>> &res, int size, int index)
    {
        if (index == size - 1)
        {
            res.push_back(nums);
        }
        for (int index2 = index; index2 < size; ++index2)
        {
            swap(nums[index], nums[index2]);
            backTrack(nums, res, size, index + 1);
            swap(nums[index], nums[index2]);
        }
    }
};
// @lc code=end
