#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (46.32%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 83K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#

# @lc code=start


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windows = {}
        sub_str = {}
        ans = []

        for c in p:
            if c in sub_str.keys():
                sub_str[c] += 1
            else:
                sub_str[c] = 1

        p_len = len(p)
        for i in range(len(s)):
            if i >= p_len:
                windows[s[i-p_len]] -= 1
                if windows[s[i-p_len]] == 0:
                    windows.pop(s[i-p_len])

            if s[i] in windows.keys():
                windows[s[i]] += 1
            else:
                windows[s[i]] = 1

            if i >= p_len-1 and windows == sub_str:
                ans.append(i-p_len+1)

        return ans

# @lc code=end
