#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (57.02%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
#
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        f0 = -prices[0]
        f1 = 0
        f2 = 0

        for price in prices[1:]:
            f0_new = max(f0, f2-price)
            f1_new = f0+price
            f2_new = max(f1, f2)

            f0 = f0_new
            f1 = f1_new
            f2 = f2_new

        return max(f1, f2)
# 我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]；
# 我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]；
# 我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]。
# 这里的「处于冷冻期」指的是在第 ii天结束之后的状态。
# 也就是说：如果第 i 天结束之后处于冷冻期，那么第 i+1 天无法买入股票。
# @lc code=end