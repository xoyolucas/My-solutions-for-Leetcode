#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.08%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    50.9K
# Total Submissions: 83.2K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def search(index, residual, path):
            if residual == 0:
                res.append(path.copy()) # 深拷贝
                return

            for i in range(index, size):
                if candidates[i] > residual:
                    break

                # 重复解跳过
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # 回溯
                path.append(candidates[i])
                search(i + 1, residual - candidates[i], path)
                path.pop()

        size = len(candidates)
        res = []
        if size == 0:
            return res

        candidates.sort()  # 排序
        search(0, target, [])
        return res


# @lc code=end
