#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (25.04%)
# Likes:    583
# Dislikes: 0
# Total Accepted:    78.7K
# Total Submissions: 313.7K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
#
# 题目数据保证答案肯定是一个 32 位的整数。
#
#
#
# 示例 1：
#
#
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#
# 示例 2：
#
#
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#
# 示例 3：
#
#
# 输入：s = "0"
# 输出：0
#
#
# 示例 4：
#
#
# 输入：s = "1"
# 输出：1
#
#
# 示例 5：
#
#
# 输入：s = "2"
# 输出：1
#
#
#
#
# 提示：
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。
#
#
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 对头部进行预处理
        dp = [0, 1]+[0]*len(s)
        s = '99'+s

        for i in range(2,len(s)):
            # 可单独解码
            if s[i] != '0':
                dp[i] += dp[i-1]
            # 可以与前一位组成两位数解码,‘04’之类的是不可解码的
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]

        return dp[-1]
# @lc code=end
