#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.39%)
# Likes:    656
# Dislikes: 0
# Total Accepted:    185.1K
# Total Submissions: 287.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#

# @lc code=start
class Solution:
    def parition(self, nums, left, right):
        pivotIndex = left
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

        for i in range(left, right + 1):
            if nums[i] < pivotValue:
                nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
                pivotIndex += 1
        nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]

        return pivotIndex

    def quickSelect(self, nums, left, right, index):
        pivot = self.parition(nums, left, right)
        if pivot == index:
            return nums[pivot]
        elif pivot < index:
            return self.quickSelect(nums, pivot + 1, right, index)
        else:
            return self.quickSelect(nums, left, pivot - 1, index)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)


# @lc code=end

