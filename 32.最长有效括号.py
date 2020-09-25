#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (33.83%)
# Likes:    982
# Dislikes: 0
# Total Accepted:    103.5K
# Total Submissions: 305.6K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#
#

# @lc code=start


class Solution:
    # 栈
    # def longestValidParentheses(self, s: str) -> int:
    #     ans = 0
    #     stack = [-1]

    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #             if len(stack) == 0:
    #                 stack.append(i)
    #             else:
    #                 ans = max(ans, i-stack[-1])

    #     return ans

    # 动态规划
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        dp = [0]*len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2 if i >= 2 else 2
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1]+(dp[i-dp[i-1]-2]+2 if i >= 2 else 2)
        return max(dp)
# @lc code=end
