#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (41.52%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 92.3K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
#
#
#
# 示例：
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
import heapq


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for i in range(n+1)]

            def lowbit(self, index):
                return index & (-index)

            # 单点更新，
            def update(self, index):
                while index <= self.size:
                    self.tree[index] += 1
                    index += self.lowbit(index)

            # 查询小于等于index的元素个数，前缀和
            def query(self, index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= self.lowbit(index)
                return res

        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        # 去重，离散化
        unique = list(set(nums))
        unique_len=len(unique)
        heapq.heapify(unique)

        # 排序映射
        rank_map = {}
        rank = 1
        for i in range(unique_len):
            rank_map[heapq.heappop(unique)] = rank
            rank += 1

        fenwick_tree = FenwickTree(unique_len)

        # 从后向前填表
        res = [0 for i in range(size)]
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少，前缀和
            res[index] = fenwick_tree.query(rank - 1)

        return res

# @lc code=end
