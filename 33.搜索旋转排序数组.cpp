/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 *
 * https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (36.27%)
 * Likes:    527
 * Dislikes: 0
 * Total Accepted:    76.3K
 * Total Submissions: 209.5K
 * Testcase Example:  '[4,5,6,7,0,1,2]\n0'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 * 
 * ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 * 
 * 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 * 
 * 你可以假设数组中不存在重复的元素。
 * 
 * 你的算法时间复杂度必须是 O(log n) 级别。
 * 
 * 示例 1:
 * 
 * 输入: nums = [4,5,6,7,0,1,2], target = 0
 * 输出: 4
 * 
 * 
 * 示例 2:
 * 
 * 输入: nums = [4,5,6,7,0,1,2], target = 3
 * 输出: -1
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        int middle = left + (right - left) / 2;

        while (left <= right)
        {
            if (nums[middle] == target)
            {
                return middle;
            }

            if (nums[left] <= nums[middle]) //左边部分升序
            {
                if (target < nums[middle] && target >= nums[left])
                {
                    right = middle - 1;
                }
                else
                {
                    left = middle + 1;
                }
            }

            else //右边部分升序
            {
                if (target <= nums[right] && target > nums[middle])
                {
                    left = middle + 1;
                }
                else
                {
                    right = middle - 1;
                }
            }

            middle = left + (right - left) / 2;
        }

        return -1; //没有找到target
    }
};
// @lc code=end
