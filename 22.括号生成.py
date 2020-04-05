#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.77%)
# Likes:    833
# Dislikes: 0
# Total Accepted:    93K
# Total Submissions: 126.1K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backTracking(str="", N=n, left=0, right=0):
            if len(str) == N * 2:
                res.append(str)
                return
            
            # 如果我们还剩一个位置，我们可以开始放一个左括号。 
            # 如果它不超过左括号的数量，我们可以放一个右括号
            if left < N:
                backTracking(str+"(", n, left + 1, right)
            if left > right:
                backTracking(str+")", n, left, right + 1)

        backTracking()
        return res


# @lc code=end
