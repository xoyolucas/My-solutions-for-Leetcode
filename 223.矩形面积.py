#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
# https://leetcode-cn.com/problems/rectangle-area/description/
#
# algorithms
# Medium (43.98%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 34.2K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
#
# 每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
#
#
#
# 示例:
#
# 输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
#
# 说明: 假设矩形面积不会超出 int 的范围。
#
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 调整两个矩形位置, 让第一个矩形ABCD靠最左边
        if A > E:
            return self.computeArea(E, F, G, H, A, B, C, D)

        area = abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 没有重叠的情况
        if B >= H or D <= F or C <= E:
            return area

        # 存在重叠情况
        # 下边界
        down = max(A, E)
        # 上
        up = min(C, G)
        # 左
        left = max(B, F)
        # 右
        right = min(D, H)

        return area - abs(up - down) * abs(left - right)

# @lc code=end