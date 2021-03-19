#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (73.70%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    63.4K
# Total Submissions: 86K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrace(k, n, cur, index):
            if len(total) == k and cur == n:
                # 注意要深拷贝
                res.append(total[:])
            if len(total) > k or cur > n:
                return

            for i in range(index, 10):
                total.append(i)
                cur += i
                backtrace(k, n, cur, i+1)
                total.pop()
                cur -= i

        res = []
        total = []
        backtrace(k, n, 0, 1)
        return res
# @lc code=end
