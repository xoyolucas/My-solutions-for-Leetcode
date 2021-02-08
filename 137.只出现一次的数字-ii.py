#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (68.44%)
# Likes:    491
# Dislikes: 0
# Total Accepted:    49.1K
# Total Submissions: 71.7K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#

# @lc code=start

# 为了区分出现一次的数字和出现三次的数字，使用两个位掩码：seen_once 和 seen_twice。
# 思路是：
# 仅当 seen_twice 未变时，改变 seen_once。
# 仅当 seen_once 未变时，改变seen_twice。


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

# @lc code=end
