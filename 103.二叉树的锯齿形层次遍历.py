#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.11%)
# Likes:    282
# Dislikes: 0
# Total Accepted:    76.2K
# Total Submissions: 138.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回锯齿形层次遍历如下：
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
from queue import Queue


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = Queue(maxsize=0)
        if root:
            q.put(root)

        l2r = True
        while not q.empty():
            size = q.qsize()
            tmp_res = [0] * size
            for i in range(size):
                root = q.get()
                tmp_res[i if l2r else size - i - 1] = root.val
                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)

            res.append(tmp_res)
            l2r = not l2r

        return res


# @lc code=end

