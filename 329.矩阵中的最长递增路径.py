#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (46.19%)
# Likes:    394
# Dislikes: 0
# Total Accepted:    38.7K
# Total Submissions: 83.7K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
#
# 示例 2:
#
# 输入: nums =
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#
#
#

# @lc code=start

# 方法一：记忆化深度优先搜索
# 方法二：拓扑排序
class Solution:
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(x, y):
            best = 1
            for dx, dy in self.direction:
                new_x = x+dx
                new_y = y+dy
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                    best = max(best, 1+dfs(new_x, new_y))

            return best

        return max([dfs(i, j) for i in range(m) for j in range(n)])

# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         if not matrix or not matrix[0]:
#             return 0
#
#         m, n = len(matrix), len(matrix[0])
#         lst = []
#         for i in range(m):
#             for j in range(n):
#                 lst.append((matrix[i][j], i, j))
#         lst.sort()
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         for num, i, j in lst:
#             dp[i][j] = 1
#             for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 r, c = i + di, j + dj
#                 if 0 <= r < m and 0 <= c < n:
#                     if matrix[i][j] > matrix[r][c]:
#                         dp[i][j] = max(dp[i][j], 1 + dp[r][c])
#         return max([dp[i][j] for i in range(m) for j in range(n)])

# @lc code=end
