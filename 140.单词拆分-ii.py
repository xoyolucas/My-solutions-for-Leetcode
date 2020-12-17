#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (44.13%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    38.2K
# Total Submissions: 86.5K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
#
#
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#
#
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index):
            if index == len(s):
                return [[]]

            res = []
            for i in range(index+min_len, index+max_len+1):
                word = s[index:i]
                if word in wordDict_hash:
                    backtrack_ans = backtrack(i)
                    for x in backtrack_ans:
                        res.append([word]+x)
            return res

        # 特例判断
        if len(wordDict) == 0:
            return []

        # 字典中单词最短和最长
        min_len = len(wordDict[0])
        max_len = len(wordDict[0])
        for i in range(len(wordDict)):
            max_len = max(max_len, len(wordDict[i]))
            min_len = min(min_len, len(wordDict[i]))

        # 将wordDict进行hash
        wordDict_hash = set(wordDict)
        res = backtrack(0)
        return [" ".join(words) for words in res]
# @lc code=end
