#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.33%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    80.4K
# Total Submissions: 204.4K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#

# @lc code=start
class Solution:
    def binarySearch(self, nums, target, findLeft):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target or (findLeft and nums[mid] == target):
                right = mid
            else:
                left = mid + 1

        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.binarySearch(nums, target, True)

        if left_index>=len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = self.binarySearch(nums, target, False) - 1

        return [left_index, right_index]


# @lc code=end
