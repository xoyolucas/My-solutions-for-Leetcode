/*
 * @lc app=leetcode.cn id=219 lang=cpp
 *
 * [219] 存在重复元素 II
 *
 * https://leetcode-cn.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (37.02%)
 * Likes:    134
 * Dislikes: 0
 * Total Accepted:    31.7K
 * Total Submissions: 85.3K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
 * 的差的绝对值最大为 k。
 * 
 * 示例 1:
 * 
 * 输入: nums = [1,2,3,1], k = 3
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入: nums = [1,0,1,1], k = 1
 * 输出: true
 * 
 * 示例 3:
 * 
 * 输入: nums = [1,2,3,1,2,3], k = 2
 * 输出: false
 * 
 */

// @lc code=start
class Solution
{
public:
    bool containsNearbyDuplicate(vector<int> &nums, int k)
    {
        unordered_set<int> tmp;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (tmp.find(nums[i]) != tmp.end())
            {
                return true;
            }
            tmp.insert(nums[i]);
            if (tmp.size() > k)
            {
                tmp.erase(nums[i - k]);
            }
        }
        return false;
    }
};

// 遍历数组，对于每个元素做以下操作：
// 在散列表中搜索当前元素，如果找到了就返回 true。
// 在散列表中插入当前元素。
// 如果当前散列表的大小超过了 kk， 删除散列表中最旧的元素。
// 返回 false。
// @lc code=end
