#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Medium (40.10%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 150.6K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#
#
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#
#
# 注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。
#
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        isInsert = False
        left, right = newInterval

        for element in intervals:
            # 元素在插入区间的左侧且无交集
            if element[1] < left:
                res.append(element)
            # 元素在插入区间的右侧且无交集
            elif element[0] > right:
                # 新区间还未插入，则直接插入新区间
                if not isInsert:
                    res.append([left, right])
                    isInsert = True
                res.append(element)
            # 与插入区间有交集，计算它们的并集
            else:
                left = min(element[0], left)
                right = max(element[1], right)

        # 新区间在所有原有区间之后
        if not isInsert:
            res.append([left, right])

        return res
# @lc code=end
