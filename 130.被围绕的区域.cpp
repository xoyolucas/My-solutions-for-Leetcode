/*
 * @lc app=leetcode.cn id=130 lang=cpp
 *
 * [130] 被围绕的区域
 *
 * https://leetcode-cn.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (40.03%)
 * Likes:    227
 * Dislikes: 0
 * Total Accepted:    37.6K
 * Total Submissions: 93.8K
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
 * 
 * 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 * 
 * 示例:
 * 
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * 
 * 
 * 运行你的函数后，矩阵变为：
 * 
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 * 
 * 
 * 解释:
 * 
 * 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
 * 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    void solve(vector<vector<char>> &board)
    {
        if (board.size() <= 2 || board[0].size() <= 2)
            return;
        int m = board.size();
        int n = board[0].size();
        for (int i = 0; i < n; i++)
        {
            bfs(board, 0, i);
        }
        for (int i = 1; i < m; i++)
        {
            bfs(board, i, n - 1);
        }
        for (int i = n - 2; i >= 0; i--)
        {
            bfs(board, m - 1, i);
        }
        for (int i = m - 2; i > 0; i--)
        {
            bfs(board, i, 0);
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (board[i][j] == 'O')
                {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '@')
                {
                    board[i][j] = 'O';
                }
            }
        }
    }

    void bfs(vector<vector<char>> &board, int i, int j)
    {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] == 'X' || board[i][j] == '@')
        {
            return;
        }
        board[i][j] = '@';
        bfs(board, i - 1, j); //上
        bfs(board, i + 1, j); //下
        bfs(board, i, j - 1); //左
        bfs(board, i, j + 1); //右
    }
};
// @lc code=end