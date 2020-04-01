/*
 * @lc app=leetcode.cn id=67 lang=cpp
 *
 * [67] 二进制求和
 *
 * https://leetcode-cn.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (52.34%)
 * Likes:    332
 * Dislikes: 0
 * Total Accepted:    72.6K
 * Total Submissions: 138.8K
 * Testcase Example:  '"11"\n"1"'
 *
 * 给定两个二进制字符串，返回他们的和（用二进制表示）。
 * 
 * 输入为非空字符串且只包含数字 1 和 0。
 * 
 * 示例 1:
 * 
 * 输入: a = "11", b = "1"
 * 输出: "100"
 * 
 * 示例 2:
 * 
 * 输入: a = "1010", b = "1011"
 * 输出: "10101"
 * 
 */

// @lc code=start
#include <string>
using namespace std;

class Solution
{
public:
    string addBinary(string a, string b)
    {
        int len1 = a.size();
        int len2 = b.size();

        while (len1 < len2)
        {
            a = '0' + a;
            len1++;
        }
        while (len2 < len1)
        {
            b = '0' + b;
            len2++;
        }

        for (int i = len1 - 1; i > 0; --i)
        {
            a[i] = a[i] - '0' + b[i];
            if (a[i] >= '2')
            {
                a[i] = (a[i] - '0') % 2 + '0';
                a[i - 1] = a[i - 1] + 1; //进位
            }
        }

        //首位处理
        a[0] = a[0] - '0' + b[0];
        if (a[0] >= '2')
        {
            a[0] = (a[0] - '0') % 2 + '0';
            a = '1' + a;
        }

        return a;
    }
};
// @lc code=end
