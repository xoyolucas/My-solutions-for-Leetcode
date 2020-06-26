/*
 * @lc app=leetcode.cn id=79 lang=cpp
 *
 * [79] 单词搜索
 *
 * https://leetcode-cn.com/problems/word-search/description/
 *
 * algorithms
 * Medium (41.73%)
 * Likes:    446
 * Dislikes: 0
 * Total Accepted:    64.5K
 * Total Submissions: 154.5K
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
 * 
 * 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
 * 
 * 
 * 
 * 示例:
 * 
 * board =
 * [
 * ⁠ ['A','B','C','E'],
 * ⁠ ['S','F','C','S'],
 * ⁠ ['A','D','E','E']
 * ]
 * 
 * 给定 word = "ABCCED", 返回 true
 * 给定 word = "SEE", 返回 true
 * 给定 word = "ABCB", 返回 false
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * board 和 word 中只包含大写和小写英文字母。
 * 1 <= board.length <= 200
 * 1 <= board[i].length <= 200
 * 1 <= word.length <= 10^3
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    bool exist(vector<vector<char>> &board, string word)
    {
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (dfs(board, word, i, j, 0))
                {
                    return true;
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>> &board, string &word, int x, int y, int index)
    {
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size() || word[index] != board[x][y])
        {
            return false;
        }
        if (index == word.size() - 1)
        {
            return word[index] == board[x][y];
        }

        char tmp = board[x][y];
        board[x][y] = '-';
        index += 1;
        bool res = dfs(board, word, x - 1, y, index) || dfs(board, word, x + 1, y, index) || dfs(board, word, x, y - 1, index) || dfs(board, word, x, y + 1, index);
        board[x][y] = tmp;

        return res;
    }
};
// @lc code=end
