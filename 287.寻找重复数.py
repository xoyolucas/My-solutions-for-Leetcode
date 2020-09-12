#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (65.79%)
# Likes:    815
# Dislikes: 0
# Total Accepted:    90.3K
# Total Submissions: 137.3K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
#
#
# 说明：
#
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#
#

# @lc code=start


class Solution:
    # 二分查找
    # def findDuplicate(self, nums: List[int]) -> int:
    #     # count[i]表示小于等于i的元素个数，下标可看为排好序的数组
    #     left = 1
    #     right = len(nums)-1
    #     res = 0
    #     while left <= right:
    #         mid = (left+right)//2
    #         count = 0
    #         for num in nums:
    #             count += (num <= mid)
    #         if count > mid:
    #             res = mid
    #             right = mid-1
    #         else:
    #             left = mid+1

    #     return res

    # 快慢指针
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # slow走一步，fast走两步，第一次相遇
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 求环的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
# @lc code=end