#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (42.87%)
# Likes:    554
# Dislikes: 0
# Total Accepted:    72.1K
# Total Submissions: 168.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#
#

# @lc code=start

# 动态规划


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        dp = [([0]*(n+1)) for i in range(m+1)] #二维数组，list深拷贝
        length = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    length = max(dp[i][j], length)

        return length**2
# @lc code=end
