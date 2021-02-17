#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Medium (73.92%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    180.5K
# Total Submissions: 244.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [3,2,1]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.res=[]

    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return None

    #     self.postorderTraversal(root.left)
    #     self.postorderTraversal(root.right)
    #     self.res.append(root.val)

    #     return self.res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        pre = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.right and root.right != pre:
                stack.append(root)
                root = root.right
            else:
                res.append(root.val)
                pre = root
                root = None

        return res

# @lc code=end
