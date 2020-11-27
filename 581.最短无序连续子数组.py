#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (34.84%)
# Likes:    366
# Dislikes: 0
# Total Accepted:    34.3K
# Total Submissions: 98.4K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 说明 :
#
#
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#
#

# @lc code=start


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_num = nums[0]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < max_num:
                right = i
            max_num = max(max_num, nums[i])

        min_num = nums[len(nums)-1]
        left = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_num:
                left = i
            min_num = min(min_num, nums[i])

        return 0 if right == left else right-left+1
# @lc code=end