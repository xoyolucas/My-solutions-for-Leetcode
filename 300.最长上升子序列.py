#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.20%)
# Likes:    969
# Dislikes: 0
# Total Accepted:    143.8K
# Total Submissions: 318.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#

# @lc code=start

# 动态规划
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0

#         dp = [1]*len(nums)

#         for i in range(1, len(nums)):
#             for j in range(i-1, -1, -1):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)

#         return max(dp)


# 贪心+二分查找 leetcode题解
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                index = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        index = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[index] = n
                
        return len(d)

# @lc code=end
