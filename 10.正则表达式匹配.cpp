/*
 * @lc app=leetcode.cn id=10 lang=cpp
 *
 * [10] 正则表达式匹配
 *
 * https://leetcode-cn.com/problems/regular-expression-matching/description/
 *
 * algorithms
 * Hard (29.64%)
 * Likes:    1425
 * Dislikes: 0
 * Total Accepted:    103.8K
 * Total Submissions: 345.8K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
 * 
 * '.' 匹配任意单个字符
 * '*' 匹配零个或多个前面的那一个元素
 * 
 * 
 * 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
 * 
 * 说明:
 * 
 * 
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * s = "aa"
 * p = "a*"
 * 输出: true
 * 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
 * 
 * 
 * 示例 3:
 * 
 * 输入:
 * s = "ab"
 * p = ".*"
 * 输出: true
 * 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 * 
 * 
 * 示例 4:
 * 
 * 输入:
 * s = "aab"
 * p = "c*a*b"
 * 输出: true
 * 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
 * 
 * 
 * 示例 5:
 * 
 * 输入:
 * s = "mississippi"
 * p = "mis*is*p*."
 * 输出: false
 * 
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    bool isMatch(string s, string p)
    {
        if (s.empty() && p.empty())
            return true;
        if (!s.empty() && p.empty())
            return false;
        if (s.empty())
        {
            // 如果正则串长度为奇数，必定不匹配，比如 "."、"ab*",必须是 a*b*这种形式，*在奇数位上
            if (p.size() % 2 != 0)
                return false;
            int i = 1;
            while (i < p.size())
            {
                if (p[i] != '*')
                    return false;
                i += 2;
            }
            return true;
        }

        int m = s.size();
        int n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        for (int i = 0; i <= m; i++)
        {
            for (int j = 0; j <= n; j++)
            {
                //分成空正则和非空正则两种
                if (j == 0)
                {
                    dp[i][j] = (i == 0);
                }
                else
                {
                    //非空正则分为两种情况 * 和 非*
                    if (p[j - 1] != '*')
                    {
                        if (i > 0 && (s[i - 1] == p[j - 1] || p[j - 1] == '.'))
                        {
                            dp[i][j] = dp[i - 1][j - 1];
                        }
                    }
                    else
                    {
                        //碰到 * 了，分为看和不看两种情况
                        //不看
                        if (j >= 2)
                        {
                            dp[i][j] = dp[i][j - 2];
                        }
                        //看
                        if (i >= 1 && j >= 2 && (s[i - 1] == p[j - 2] || p[j - 2] == '.'))
                        {
                            dp[i][j] = (dp[i][j] || dp[i - 1][j]);
                        }
                    }
                }
            }
        }

        return dp[m][n];
    }
};
// @lc code=end
