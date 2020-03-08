/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 *
 * https://leetcode-cn.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (60.98%)
 * Likes:    283
 * Dislikes: 0
 * Total Accepted:    54.7K
 * Total Submissions: 89.7K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
 * 
 * 示例:
 * 
 * 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
 * 输出:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 * 
 * 说明：
 * 
 * 
 * 所有输入均为小写字母。
 * 不考虑答案输出的顺序。
 * 
 * 
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> res_map;
        vector<vector<string>> res;
        for (auto &str : strs)
        {
            string tmp = str;
            sort(tmp.begin(), tmp.end()); //排序后相等
            res_map[tmp].emplace_back(str); //排序后作为key，映射
        }
        for (auto &element : res_map)
        {
            res.emplace_back(element.second);
        }
        return res;
    }
};
// @lc code=end
