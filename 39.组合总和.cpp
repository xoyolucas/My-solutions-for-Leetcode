/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 *
 * https://leetcode-cn.com/problems/combination-sum/description/
 *
 * algorithms
 * Medium (67.90%)
 * Likes:    540
 * Dislikes: 0
 * Total Accepted:    65.5K
 * Total Submissions: 95.8K
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 * 
 * candidates 中的数字可以无限制重复被选取。
 * 
 * 说明：
 * 
 * 
 * 所有数字（包括 target）都是正整数。
 * 解集不能包含重复的组合。 
 * 
 * 
 * 示例 1:
 * 
 * 输入: candidates = [2,3,6,7], target = 7,
 * 所求解集为:
 * [
 * ⁠ [7],
 * ⁠ [2,2,3]
 * ]
 * 
 * 
 * 示例 2:
 * 
 * 输入: candidates = [2,3,5], target = 8,
 * 所求解集为:
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
 * ]
 * 
 */

// @lc code=start
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        sort(candidates.begin(), candidates.end());
        this->candidates = candidates;
        DFS(0, target);
        return res;
    }

    void DFS(int index, int target)
    {
        if (target == 0)
        {
            res.push_back(path);
        }
        for (int i = index; i < candidates.size() && target - candidates[i] >= 0; ++i)
        {
            path.push_back(candidates[i]);
            DFS(i, target - candidates[i]);
            path.pop_back();
        }
    }

private:
    vector<vector<int>> res;
    vector<int> path;
    vector<int> candidates;
};
// @lc code=end