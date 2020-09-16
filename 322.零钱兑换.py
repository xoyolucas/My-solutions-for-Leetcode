#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (41.34%)
# Likes:    818
# Dislikes: 0
# Total Accepted:    134.6K
# Total Submissions: 325.6K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
#
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#

# @lc code=start

# 动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return -1

        # dp[j]代表当钱包的总价值为j时，所需要的最少硬币的个数
        dp = [0x7fffffff]*(amount+1)
        dp[0] = 0

        # 当外层循环执行一次以后，说明在只使用前i个硬币的情况下，各个钱包的最少硬币个数已经得到，
        for coin in coins:
            for i in range(coin, amount+1):
                # 对于任意金额j,dp[i] = min(dp[i],dp[i-coin]+1),如果i-coin存在的话.
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != 0x7fffffff else -1
    
# BFS
# @lc code=end
