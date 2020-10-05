#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (48.47%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 32K
# Testcase Example:  '"()())()"'
#
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
#
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
#
# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
#
#
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
#
#
# 示例 3:
#
# 输入: ")("
# 输出: [""]
#
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False  # 只用count出现了负值，终止循环，已经出现非法字符
            return count == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid:
                return valid  # 如果当前valid是非空的，说明已经有合法的产生了
                
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":  # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1 :])
            level = next_level


# @lc code=end

