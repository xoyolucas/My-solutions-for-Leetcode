#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (56.37%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    65.9K
# Total Submissions: 117K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = collections.deque()
        level.append(root)
        res = 0

        while len(level) > 0:
            cur = level.popleft()
            if cur.left:
                if cur.left.left == None and cur.left.right == None:
                    res += cur.left.val
                else:
                    level.append(cur.left)
            if cur.right:
                level.append(cur.right)

        return res

# @lc code=end
