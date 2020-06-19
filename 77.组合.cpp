/*
 * @lc app=leetcode.cn id=77 lang=cpp
 *
 * [77] 组合
 *
 * https://leetcode-cn.com/problems/combinations/description/
 *
 * algorithms
 * Medium (73.86%)
 * Likes:    290
 * Dislikes: 0
 * Total Accepted:    55.7K
 * Total Submissions: 75.4K
 * Testcase Example:  '4\n2'
 *
 * 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
 * 
 * 示例:
 * 
 * 输入: n = 4, k = 2
 * 输出:
 * [
 * ⁠ [2,4],
 * ⁠ [3,4],
 * ⁠ [2,3],
 * ⁠ [1,2],
 * ⁠ [1,3],
 * ⁠ [1,4],
 * ]
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> res;
    void backtrack(vector<int> &vec, int begin, int k, int n)
    {
        if (vec.size() == k)
        {
            res.emplace_back(vec);
        }
        if (vec.size() + (n - begin + 1) < k)
        {
            return;
        }

        for (int i = begin; i <= n; i++)
        {
            vec.emplace_back(i);
            backtrack(vec, i + 1, k, n);
            vec.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k)
    {
        vector<int> vec;
        backtrack(vec, 1, k, n);
        return res;
    }
};
// @lc code=end
