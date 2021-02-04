#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.94%)
# Likes:    436
# Dislikes: 0
# Total Accepted:    84.8K
# Total Submissions: 119.5K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recursive(left_index, right_index):
            nonlocal post_index
            if left_index > right_index:
                return None

            # 根节点的value
            val = postorder[post_index]
            post_index -= 1
            # 构造根节点
            root = TreeNode(val)
            # 根节点在中序遍历中的位置
            root_index = idx_map[val]

            # 右子树
            root.right = recursive(root_index+1, right_index)
            # 左子树
            root.left = recursive(left_index, root_index-1)

            return root

        idx_map = {val: idx for idx, val in enumerate(inorder)}
        post_index = len(postorder)-1
        return recursive(0, len(inorder)-1)
    

# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         """
#         :type inorder: List[int]
#         :type postorder: List[int]
#         :rtype: TreeNode
#         """
#         if not postorder:
#             return None
#         root = TreeNode(postorder[-1])#创建树
#         n = inorder.index(root.val)
#         root.left = self.buildTree(inorder[:n],postorder[:n])
#         root.right = self.buildTree(inorder[n+1:],postorder[n:-1])
#         return root
# @lc code=end
