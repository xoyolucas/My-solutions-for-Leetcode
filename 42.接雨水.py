#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (52.63%)
# Likes:    1672
# Dislikes: 0
# Total Accepted:    149.9K
# Total Submissions: 284.7K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#

# @lc code=start


class Solution:
    # 双指针
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0

        left = 0
        right = length-1
        left_max = 0
        right_max = 0
        ans = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                ans += left_max-height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max-height[right]
                right -= 1

        return ans

    # 单调栈
    # def trap(self, height: List[int]) -> int:
    #     length = len(height)
    #     if length < 3:
    #         return 0
    #     res, idx = 0, 0
    #     stack = []
    #     while idx < length:
    #         while len(stack) > 0 and height[idx] > height[stack[-1]]:
    #             top = stack.pop()  # index of the last element in the stack
    #             if len(stack) == 0:
    #                 break
    #             h = min(height[stack[-1]], height[idx]) - height[top]
    #             dist = idx - stack[-1] - 1
    #             res += (dist * h)
    #         stack.append(idx)
    #         idx += 1
    #     return res

# @lc code=end
