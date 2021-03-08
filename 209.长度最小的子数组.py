#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.82%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    109.9K
# Total Submissions: 245.1K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
#
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#
#
# 进阶：
#
#
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#
#

# @lc code=start
class Solution:
    # 滑动窗口
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum = 0
        start, end = 0, 0
        size = len(nums)
        res = size+1

        # 右移end指针，增加总和
        while end < size:
            sum += nums[end]

            # 右移start指针，保证sum>=s情况下，缩小子数组长度
            while sum >= s:
                res = min(res, end-start+1)
                sum -= nums[start]
                start += 1

            end += 1

        return res if res != size+1 else 0
# @lc code=end
