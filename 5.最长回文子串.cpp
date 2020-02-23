/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (28.08%)
 * Likes:    1622
 * Dislikes: 0
 * Total Accepted:    165.1K
 * Total Submissions: 587.9K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 * 
 * 示例 1：
 * 
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入: "cbbd"
 * 输出: "bb"
 * 
 * 
 */

// @lc code=start
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        const int len = s.length();
        if (len == 0)
            return "";
        string origin_str = s;
        string reverse_str = s;
        reverse(reverse_str.begin(), reverse_str.end());
        vector<vector<int>> m(len, vector<int>(len));
        int max_len = 0;
        int str_end = 0;

        for (int i = 0; i < len; ++i)
        {
            for (int j = 0; j < len; ++j)
            {
                if (origin_str[i] == reverse_str[j])
                {
                    if (i == 0 || j == 0)
                    {
                        m[i][j] = 1;
                    }
                    else
                    {
                        m[i][j] = m[i - 1][j - 1] + 1;
                    }
                }
                // 更新当前最长的回文数
                if (m[i][j] > max_len)
                {
                    int origin_index = len - 1 - j;
                    if (origin_index + m[i][j] - 1 == i) //判断是否回文
                    {
                        max_len = m[i][j];
                        str_end = i;
                    }
                }
            }
        }
         //其内容被初始化成字符串s的第str_end - max_len + 1个字符开始的连续max_len个字符。
        return string(s, str_end - max_len + 1, max_len);
    }
};
// @lc code=end
