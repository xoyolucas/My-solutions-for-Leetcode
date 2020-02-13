/*
 * @lc app=leetcode.cn id=1260 lang=cpp
 *
 * [1260] 二维网格迁移
 *
 * https://leetcode-cn.com/problems/shift-2d-grid/description/
 *
 * algorithms
 * Easy (57.55%)
 * Likes:    12
 * Dislikes: 0
 * Total Accepted:    3.4K
 * Total Submissions: 5.9K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
 *
 * 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
 * 
 * 每次「迁移」操作将会引发下述活动：
 * 
 * 
 * 位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
 * 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
 * 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
 * 
 * 
 * 请你返回 k 次迁移操作后最终得到的 二维网格。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
 * 输出：[[9,1,2],[3,4,5],[6,7,8]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
 * 输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
 * 
 * 
 * 示例 3：
 * 
 * 输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
 * 输出：[[1,2,3],[4,5,6],[7,8,9]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= grid.length <= 50
 * 1 <= grid[i].length <= 50
 * -1000 <= grid[i][j] <= 1000
 * 0 <= k <= 100
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <deque>
using namespace std;

class Solution
{
public:
    vector<vector<int>> shiftGrid(vector<vector<int>> &grid, int k)
    {
        deque<int> dequeGrid;
        for (auto &row : grid)
        {
            for (auto &num : row)
            {
                dequeGrid.push_back(num);
            }
        }
        for (int i = 0; i < k; ++i)
        {
            int back = dequeGrid.back();
            dequeGrid.pop_back();
            dequeGrid.push_front(back);
        }

        for (int i = 0, k = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid[i].size(); ++j)
            {
                grid[i][j] = dequeGrid.at(k++);
            }
        }

        return grid;
    }
};

//使用双向队列，转为1维数组，移动k次后再转回二维数组
// 先将二维网格线性成一维的双向队列
// 执行k次操作：将双向队列的最后一个数字压入到队列的前面，弹出队列内的最后一个数字；
// 最后将一维的双向队列重新转换成二维的网格即可
// @lc code=end
