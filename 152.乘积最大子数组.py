#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (40.28%)
# Likes:    757
# Dislikes: 0
# Total Accepted:    93.6K
# Total Submissions: 232.5K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0

        ans = nums[0]
        dp_max = nums[0]
        dp_min = nums[0]

        for num in nums[1:]:
            dp_min_tmp, dp_max_tmp = dp_min, dp_max
            dp_min = min(num, dp_min_tmp * num, dp_max_tmp * num)
            dp_max = max(num, dp_min_tmp * num, dp_max_tmp * num)
            ans = max(ans, dp_max)

        return ans


# @lc code=end

