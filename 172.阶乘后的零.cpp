/*
 * @lc app=leetcode.cn id=172 lang=cpp
 *
 * [172] 阶乘后的零
 *
 * https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
 *
 * algorithms
 * Easy (39.42%)
 * Likes:    195
 * Dislikes: 0
 * Total Accepted:    25.9K
 * Total Submissions: 65.6K
 * Testcase Example:  '3'
 *
 * 给定一个整数 n，返回 n! 结果尾数中零的数量。
 * 
 * 示例 1:
 * 
 * 输入: 3
 * 输出: 0
 * 解释: 3! = 6, 尾数中没有零。
 * 
 * 示例 2:
 * 
 * 输入: 5
 * 输出: 1
 * 解释: 5! = 120, 尾数中有 1 个零.
 * 
 * 说明: 你算法的时间复杂度应为 O(log n) 。
 * 
 */

// @lc code=start
class Solution
{
public:
    int trailingZeroes(int n)
    {
        int result = 0;
        while (n / 5 != 0)
        {
            result += n / 5;
            n /= 5;
        }
        return result;
    }
};

// 不断除以 5, 是因为每间隔 5 个数有一个数可以被 5 整除, 然后在这些可被 5 整除的数中, 
// 每间隔 5 个数又有一个可以被 25 整除, 故要再除一次, 直到结果为 0, 表示没有能继续被 5 整除的数了.
// @lc code=end
