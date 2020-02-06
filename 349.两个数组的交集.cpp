/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
 *
 * https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
 *
 * algorithms
 * Easy (67.65%)
 * Likes:    157
 * Dislikes: 0
 * Total Accepted:    49.1K
 * Total Submissions: 72.3K
 * Testcase Example:  '[1,2,2,1]\n[2,2]'
 *
 * 给定两个数组，编写一个函数来计算它们的交集。
 * 
 * 示例 1:
 * 
 * 输入: nums1 = [1,2,2,1], nums2 = [2,2]
 * 输出: [2]
 * 
 * 
 * 示例 2:
 * 
 * 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 * 输出: [9,4]
 * 
 * 说明:
 * 
 * 
 * 输出结果中的每个元素一定是唯一的。
 * 我们可以不考虑输出结果的顺序。
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> set_tmp(nums1.begin(), nums1.end()); //将第一个数组转为unordered_set
        vector<int> res;

        for (int n : nums2)
        {
            if (set_tmp.erase(n)) //既查找了m中是否存在a,又完成了删除a的工作，避免后续重复元素
            {
                res.push_back(n);
            }
        }
        return res;
    }
};
//python return list(set(nums1) & set(nums2))
// @lc code=end
