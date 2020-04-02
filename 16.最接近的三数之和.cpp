/*
 * @lc app=leetcode.cn id=16 lang=cpp
 *
 * [16] 最接近的三数之和
 *
 * https://leetcode-cn.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (43.55%)
 * Likes:    391
 * Dislikes: 0
 * Total Accepted:    87.7K
 * Total Submissions: 201.4K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
 * 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
 * 
 * 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
 * 
 * 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
 * 
 * 
 */

// @lc code=start
class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        if (nums.size() < 3)
        {
            return 0;
        }

        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.size() - 2; ++i)
        {
            int first = i + 1;
            int second = nums.size() - 1;

            if (nums[i] > 0 && nums[i] > target)
            {
                break;
            }

            while (first < second)
            {
                int sum = nums[i] + nums[first] + nums[second];
                if (sum == target)
                {
                    return target;
                }
                if (abs(target - sum) < abs(target - res))
                {
                    res = sum;
                }
                if (sum < target)
                {
                    first++;
                }
                if (sum > target)
                {
                    second--;
                }
            }
        }

        return res;
    }
};
// @lc code=end