/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 *
 * https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (53.04%)
 * Likes:    645
 * Dislikes: 0
 * Total Accepted:    96.5K
 * Total Submissions: 181.9K
 * Testcase Example:  '"23"'
 *
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 * 
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * 
 * 
 * 
 * 示例:
 * 
 * 输入："23"
 * 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * 
 * 
 * 说明:
 * 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
 * 
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    vector<string> letterCombinations(string digits)
    {
        if (digits.empty())
        {
            return res;
        }

        vector<string> letter_map = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        string str = "";

        combine(digits, letter_map, 0, str);

        return res;
    }

    void combine(string &digits, vector<string> &letter_map, int index, string &str)
    {
        if (index == digits.size())
        {
            res.push_back(str);
            return;
        }

        int n = digits[index] - '2';

        for (int i = 0; i < letter_map[n].size(); ++i)
        {
            str += letter_map[n][i];
            combine(digits, letter_map, index + 1, str);
            str.erase(str.end() - 1);
        }
    }

private:
    vector<string> res;
};
// @lc code=end
