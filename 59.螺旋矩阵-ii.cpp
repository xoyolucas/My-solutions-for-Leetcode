/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 *
 * https://leetcode-cn.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (76.95%)
 * Likes:    171
 * Dislikes: 0
 * Total Accepted:    30.8K
 * Total Submissions: 40K
 * Testcase Example:  '3'
 *
 * 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
 * 
 * 示例:
 * 
 * 输入: 3
 * 输出:
 * [
 * ⁠[ 1, 2, 3 ],
 * ⁠[ 8, 9, 4 ],
 * ⁠[ 7, 6, 5 ]
 * ]
 * 
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<int>> generateMatrix(int n)
    {
        vector<vector<int>> res(n, vector<int>(n, 0));
        int left = 0, right = n - 1, top = 0, bottom = n - 1;
        int num = 1;

        while (num <= n * n)
        {
            for (int i = left; i <= right; ++i)
            {
                res[top][i] = num++;
            }
            top++;
            for (int i = top; i <= bottom; ++i)
            {
                res[i][right] = num++;
            }
            right--;
            for (int i = right; i >= left; --i)
            {
                res[bottom][i] = num++;
            }
            bottom--;
            for (int i = bottom; i >= top; --i)
            {
                res[i][left] = num++;
            }
            left++;
        }

        return res;
    }
};
// @lc code=end
