/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 *
 * https://leetcode-cn.com/problems/4sum/description/
 *
 * algorithms
 * Medium (37.35%)
 * Likes:    424
 * Dislikes: 0
 * Total Accepted:    67.8K
 * Total Submissions: 181.5K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
 * + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
 * 
 * 注意：
 * 
 * 答案中不可以包含重复的四元组。
 * 
 * 示例：
 * 
 * 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
 * 
 * 满足要求的四元组集合为：
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target)
    {
        vector<vector<int>> res;

        if (nums.size() < 4)
        {
            return res;
        }

        sort(nums.begin(), nums.end());
        int a,b,c,d,sum;

        for (a = 0; a < nums.size() - 3; ++a)
        {
            if (a > 0 && nums[a] == nums[a - 1]) //避免重复
            {
                continue;
            }
            for (b = a + 1; b < nums.size() - 2; ++b)
            {
                if (b > a + 1 && nums[b] == nums[b - 1]) //避免重复
                {
                    continue;
                }
                c = b + 1;
                d = nums.size() - 1;
                while (c < d)
                {
                    sum = nums[a] + nums[b] + nums[c] + nums[d];
                    if (sum < target)
                    {
                        c++;
                    }
                    else if (sum > target)
                    {
                        d--;
                    }
                    else
                    {
                        res.push_back({nums[a], nums[b], nums[c], nums[d]});
                        while (c < d && nums[c] == nums[c + 1]) //确保nums[c]改变
                        {
                            c++;
                        }
                        while (c < d && nums[d] == nums[d - 1]) //确保nums[d]改变
                        {
                            d--;
                        }
                        c++;
                        d--;
                    }
                }
            }
        }

        return res;
    }
};
// @lc code=end
