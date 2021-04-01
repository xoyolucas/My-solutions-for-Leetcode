#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (44.92%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 56.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：[3,2,3]
# 输出：[3]
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：[1]
#
#
# 示例 3：
#
#
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
#
#
#
# 提示：
#
#
# 1
# -10^9
#
#
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票法
        if len(nums) == 0:
            return None

        res = []
        candidate1, candidate2 = nums[0], nums[0]
        count1, count2 = 0, 0

        #  摩尔投票法，分为两个阶段：配对阶段和计数阶段
        #  配对阶段
        for num in nums:
            if candidate1 == num:
                count1 += 1
                continue
            if candidate2 == num:
                count2 += 1
                continue

            # 和当前num不匹配
            if count1 == 0:
                candidate1 = num
                count1 = 1
                continue
            if count2 == 0:
                candidate2 = num
                count2 = 1
                continue

            count1 -= 1
            count2 -= 1

        # 计数阶段
        # 找到了两个候选人之后，需要确定票数是否满足大于 N/3
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        if count1 > len(nums)/3:
            res.append(candidate1)
        if count2 > len(nums)/3:
            res.append(candidate2)

        return res
# @lc code=end
