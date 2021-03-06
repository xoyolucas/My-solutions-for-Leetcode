/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
 *
 * https://leetcode-cn.com/problems/word-break/description/
 *
 * algorithms
 * Medium (44.84%)
 * Likes:    458
 * Dislikes: 0
 * Total Accepted:    56.5K
 * Total Submissions: 126.1K
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
 * 
 * 说明：
 * 
 * 
 * 拆分时可以重复使用字典中的单词。
 * 你可以假设字典中没有重复的单词。
 * 
 * 
 * 示例 1：
 * 
 * 输入: s = "leetcode", wordDict = ["leet", "code"]
 * 输出: true
 * 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
 * 
 * 
 * 示例 2：
 * 
 * 输入: s = "applepenapple", wordDict = ["apple", "pen"]
 * 输出: true
 * 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
 * 注意你可以重复使用字典中的单词。
 * 
 * 
 * 示例 3：
 * 
 * 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 * 输出: false
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        if (wordDict.empty())
        {
            if (!s.empty())
            {
                return false;
            }
            return true;
        }
        
        vector<bool> res(s.length() + 1, false);
        res[0] = true;
        int min = wordDict[0].size();
        int max = wordDict[0].size();
        for (int i = 1; i < wordDict.size(); i++)
        {
            max = std::max(max, (int)wordDict[i].size());
            min = std::min(min, (int)wordDict[i].size());
        }
        for (int i = min; i <= s.size(); i++)
        {
            for (int j = std::max(i - max, 0); j <= i - min; j++)
            {
                if (res[j] && std::find(wordDict.begin(), wordDict.end(), s.substr(j, i - j)) != wordDict.end())
                {
                    res[i] = true;
                    break;
                }
            }
        }

        return res[s.size()];
    }
};
// @lc code=end
