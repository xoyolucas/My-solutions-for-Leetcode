#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.66%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    62.2K
# Total Submissions: 100.9K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        tmp = []
        left = 0
        right = 0
        size = 0
        # 在之前已经生成的所有子列上依次加上新的元素，生成新的子列
        for i in range(len(nums)):
            # 去重，决定起始位置
            if i != 0:
                left = len(res)-size if nums[i] == nums[i-1] else 0
            right = len(res)
            size = right-left
            # 生成新的序列
            res += [res[j]+[nums[i]] for j in range(left, right)]

        return res

# @lc code=end
