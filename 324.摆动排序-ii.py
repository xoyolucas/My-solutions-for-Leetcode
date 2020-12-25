#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
# https://leetcode-cn.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (36.55%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 46.3K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 示例 1:
#
# 输入: nums = [1, 5, 1, 1, 6, 4]
# 输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
#
# 示例 2:
#
# 输入: nums = [1, 3, 2, 2, 3, 1]
# 输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
#
# 说明:
# 你可以假设所有输入都会得到有效的结果。
#
# 进阶:
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
#
#

# @lc code=start
import math


class Solution:
    def quickSelect(self, data_list, begin, end, k):
        length = len(data_list)
        index = self.partition(data_list, begin, end)
        while index != length - k:
            if index > length - k:
                end = index-1
                index = self.partition(data_list, begin, index-1)
            else:
                begin = index+1
                index = self.partition(data_list, index+1, end)
        return data_list[index]

    def partition(self, data_list, begin, end):
        # 选择最后一个元素作为分区键
        partition_key = data_list[end]

        # index为分区键的最终位置
        # 比partition_key小的放左边，比partition_key大的放右边
        index = begin
        for i in range(begin, end):
            if data_list[i] < partition_key:
                data_list[i], data_list[index] = data_list[index], data_list[i]
                index += 1

        data_list[index], data_list[end] = data_list[end], data_list[index]
        return index

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快速选择 + 3-way-partition
        # 找到中位数
        size = len(nums)
        mid = self.quickSelect(nums, 0, size-1, math.ceil(size/2))

        # 3-way-partition
        i = 0
        j = 0
        k = size-1
        while j < k:
            if nums[j] > mid:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1

        left = nums[math.ceil(size/2)-1::-1]
        right = nums[:math.ceil(size/2)-1:-1]
        nums[::2] = left
        nums[1::2] = right

# @lc code=end
