#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (41.68%)
# Likes:    925
# Dislikes: 0
# Total Accepted:    91K
# Total Submissions: 218.2K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        left = [0]*n
        right = [0]*n
        stack = list()

        # 从左往右扫
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        # 从右往左扫
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # 计算面积
        area = max((right[i]-left[i]-1)*heights[i] for i in range(n))

        return area

    # 只遍历数组一遍
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     n = len(heights)
    #     left, right = [0] * n, [n] * n

    #     mono_stack = list()
    #     for i in range(n):
    #         while mono_stack and heights[mono_stack[-1]] >= heights[i]:
    #             right[mono_stack[-1]] = i
    #             mono_stack.pop()
    #         left[i] = mono_stack[-1] if mono_stack else -1
    #         mono_stack.append(i)

    #     ans = max((right[i] - left[i] - 1) * heights[i]
    #               for i in range(n)) if n > 0 else 0
    #     return ans

# @lc code=end
