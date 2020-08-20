#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (60.57%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    74.3K
# Total Submissions: 122.6K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
#
#
#

# @lc code=start
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        h = []
        for pair in dict.items():
            pair=pair[::-1] #key和pair反转
            if len(h) < k:
                heapq.heappush(h, pair)
            elif len(h) == k and pair[0] > h[0][0]: #比较是否大于最小堆顶
                heapq.heappop(h)
                heapq.heappush(h, pair)

        ans = [x[1] for x in h]
        return ans
# @lc code=end