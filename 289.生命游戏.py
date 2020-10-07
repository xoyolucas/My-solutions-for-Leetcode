#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (74.46%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    39.8K
# Total Submissions: 53.5K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0
# 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 
# 
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 
# 
# 
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
# 
# 
# 
# 示例：
# 
# 输入： 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出：
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# 
# 进阶：
# 
# 
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
# 
# 
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # 遍历面板每一个格子里的细胞
        for row in range(rows):
            for col in range(cols):
                # 对于每一个细胞统计其八个相邻位置里的活细胞数量
                live_neighbors = 0

                for neighbor in neighbors:
                    # 相邻位置的坐标
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    # 查看相邻的细胞是否是活细胞
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # 过去的活细胞，现在变为死细胞
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 代表这个细胞过去是活的现在死了
                    board[row][col] = -1
                # 过去的死细胞，现在变为活细胞
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 代表这个细胞过去是死的现在活了
                    board[row][col] = 2

        # 遍历 board 刷新更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
# @lc code=end

