/*
 * @lc app=leetcode.cn id=371 lang=cpp
 *
 * [371] 两整数之和
 *
 * https://leetcode-cn.com/problems/sum-of-two-integers/description/
 *
 * algorithms
 * Easy (53.38%)
 * Likes:    188
 * Dislikes: 0
 * Total Accepted:    21.7K
 * Total Submissions: 40.5K
 * Testcase Example:  '1\n2'
 *
 * 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
 * 
 * 示例 1:
 * 
 * 输入: a = 1, b = 2
 * 输出: 3
 * 
 * 
 * 示例 2:
 * 
 * 输入: a = -2, b = 3
 * 输出: 1
 * 
 */

// @lc code=start
class Solution
{
public:
    int getSum(int a, int b)
    {
        while (b)
        {
            auto carry = ((unsigned int)(a & b)) << 1; // 记录a+b的进位，直到进位为0是退出
            a = a ^ b; //结果相加
            b = carry; //循环
        }
        return a;
    }
};

// a + b 的问题拆分为 (a 和 b 的无进位结果) + (a 和 b 的进位结果)
// 无进位加法使用异或运算计算得出
// 进位结果使用与运算和移位运算计算得出
// 循环此过程，直到进位为 0
// @lc code=end
