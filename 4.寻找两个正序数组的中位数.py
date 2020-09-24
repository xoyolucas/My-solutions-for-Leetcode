#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.78%)
# Likes:    3222
# Dislikes: 0
# Total Accepted:    262.6K
# Total Submissions: 677.2K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
#
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
#
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left_num = (m+n+1)//2

        # 寻找nums1的分割线位置 nums1[i-1]<=num2[j]&&nums2[j-1]<=nums1[j]
        left = 0
        right = m
        while left < right:
            i = left+(right-left+1)//2
            j = left_num-i
            if nums1[i-1] > nums2[j]:
                # 下一轮搜索的区间 [left, i - 1]
                right = i-1
            else:
                # 下一轮搜索的区间 [i, right]
                left = i

        i = left
        j = left_num-i
        inf = 0x7fffffff
        nums1_left_max = nums1[i-1] if i != 0 else -inf
        nums1_right_min = nums1[i] if i < m else inf
        nums2_left_max = nums2[j-1] if j != 0 else -inf
        nums2__right_min = nums2[j] if j < n else inf

        # 根据数组长度和为奇数和偶数分别计算
        if (m+n) % 2 == 1:
            return max(nums1_left_max, nums2_left_max)
        else:
            return (max(nums1_left_max, nums2_left_max)+min(nums1_right_min, nums2__right_min))/2.0
# @lc code=end
