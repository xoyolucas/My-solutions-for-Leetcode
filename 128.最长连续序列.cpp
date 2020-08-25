/*
 * @lc app=leetcode.cn id=128 lang=cpp
 *
 * [128] 最长连续序列
 *
 * https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
 *
 * algorithms
 * Hard (51.08%)
 * Likes:    479
 * Dislikes: 0
 * Total Accepted:    70.6K
 * Total Submissions: 136.6K
 * Testcase Example:  '[100,4,200,1,3,2]'
 *
 * 给定一个未排序的整数数组，找出最长连续序列的长度。
 * 
 * 要求算法的时间复杂度为 O(n)。
 * 
 * 示例:
 * 
 * 输入: [100, 4, 200, 1, 3, 2]
 * 输出: 4
 * 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
 * 
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> hash;
        for (auto num : nums)
        {
            hash.insert(num);
        }

        int best = 0;
        int local = 1;
        for (auto num : nums)
        {
            if (hash.find(num - 1) != hash.end())
            {
                continue;
            }
            local = 1;
            while (hash.find(num + local) != hash.end())
            {
                local++;
            }
            best = max(best, local);
        }

        return best;
    }
};
// @lc code=end
