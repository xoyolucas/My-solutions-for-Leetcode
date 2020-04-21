/*
 * @lc app=leetcode.cn id=43 lang=cpp
 *
 * [43] 字符串相乘
 *
 * https://leetcode-cn.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (42.06%)
 * Likes:    321
 * Dislikes: 0
 * Total Accepted:    57K
 * Total Submissions: 135.3K
 * Testcase Example:  '"2"\n"3"'
 *
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 * 
 * 示例 1:
 * 
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 * 
 * 示例 2:
 * 
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 * 
 * 说明：
 * 
 * 
 * num1 和 num2 的长度小于110。
 * num1 和 num2 只包含数字 0-9。
 * num1 和 num2 均不以零开头，除非是数字 0 本身。
 * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 * 
 * 
 */

// @lc code=start
#include <string>
using namespace std;

class Solution
{
public:
    string multiply(string num1, string num2)
    {
        int len1 = num1.size();
        int len2 = num2.size();
        string res(len1 + len2, '0');

        for (int i = len2 - 1; i >= 0; i--)
        {
            for (int j = len1 - 1; j >= 0; j--)
            {
                int temp = (res[i + j + 1] - '0') + (num1[j] - '0') * (num2[i] - '0');
                res[i + j + 1] = temp % 10 + '0'; // 当前位
                res[i + j] += temp / 10;          // 进位
            }
        }

        // 去除首位的‘0’
        for (int i = 0; i < len1 + len2; i++)
        {
            if (res[i] != '0')
            {
                return res.substr(i);
            }
        }

        return "0";
    }
};
// @lc code=end
