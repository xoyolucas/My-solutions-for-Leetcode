#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.17%)
# Likes:    723
# Dislikes: 0
# Total Accepted:    77.3K
# Total Submissions: 179K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
#
#
# 示例 1：
#
# 输入：[1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出：6
#
#
# 示例 2：
#
# 输入：[-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# 输出：42
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_gain = -0x7fffffff

        def dfsGain(node):
            # nonlocal关键字用来在函数或其它作用域中使用外层（非全局）变量
            nonlocal max_gain

            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            left_max = max(dfsGain(node.left), 0)
            right_max = max(dfsGain(node.right), 0)
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            max_gain = max(max_gain, node.val+left_max+right_max)

            # 返回节点的最大贡献值
            return node.val+max(left_max, right_max)

        dfsGain(root)
        return max_gain
# @lc code=end
