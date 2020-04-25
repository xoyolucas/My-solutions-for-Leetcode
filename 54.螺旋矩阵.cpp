/*
 * @lc app=leetcode.cn id=54 lang=cpp
 *
 * [54] 螺旋矩阵
 *
 * https://leetcode-cn.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (39.38%)
 * Likes:    338
 * Dislikes: 0
 * Total Accepted:    51.1K
 * Total Submissions: 129.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
 * 
 * 示例 1:
 * 
 * 输入:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 4, 5, 6 ],
 * ⁠[ 7, 8, 9 ]
 * ]
 * 输出: [1,2,3,6,9,8,7,4,5]
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * [
 * ⁠ [1, 2, 3, 4],
 * ⁠ [5, 6, 7, 8],
 * ⁠ [9,10,11,12]
 * ]
 * 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
 * 
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        vector<int> res;
        if (matrix.empty())
        {
            return res;
        }

        //赋值上下左右边界
        int top = 0;
        int bottom = matrix.size() - 1;
        int left = 0;
        int right = matrix[0].size() - 1;

        while (true)
        {
            for (int i = left; i <= right; ++i)
            {
                res.push_back(matrix[top][i]); //从左到右移动
            } 
            if (++top > bottom)//重新设定上边界
                break;

            for (int i = top; i <= bottom; ++i)
            {
                res.push_back(matrix[i][right]); //向上往下移动
            } 
            if (--right < left)
                break;
                
            for (int i = right; i >= left; --i)
            {
                res.push_back(matrix[bottom][i]); //从右向左移动
            }
            if (--bottom < top)
                break;
            
            for (int i = bottom; i >= top; --i)
            {
                res.push_back(matrix[i][left]); //向下往上移动
            }
            if (++left > right)
                break;
        }
        return res;
    }
};
// @lc code=end
