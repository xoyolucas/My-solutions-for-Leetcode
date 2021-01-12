#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (51.15%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    57.3K
# Total Submissions: 112K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
#
#
# 示例 1：
#
# 输入："hello"
# 输出："holle"
#
#
# 示例 2：
#
# 输入："leetcode"
# 输出："leotcede"
#
#
#
# 提示：
#
#
# 元音字母不包含字母 "y" 。
#
#
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 元音字母表
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = list(s)
        begin = 0
        end = len(s)-1

        while begin < end:
            if words[begin] in dic and words[end] in dic:
                # 交换左右指针所指元素
                words[begin], words[end] = words[end], words[begin]
                begin += 1
                end -= 1
                continue
            if words[begin] not in dic:
                begin += 1
            if words[end] not in dic:
                end -= 1

        return ''.join(words)

# @lc code=end
