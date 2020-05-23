#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (59.08%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    48.6K
# Total Submissions: 81.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        cur = []
        
        def dfs(node, sum):
            val = node.val
            rest = sum - val
            cur.append(val)
            if rest == 0 and node.left == None and node.right == None:
                res.append(cur[:])  # 注意要append cur的copy
            if node.left != None:
                dfs(node.left, rest)
            if node.right != None:
                dfs(node.right, rest)

            cur.pop()

        if root != None:
            dfs(root, sum)
        return res

## 更加简便的写法
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         if not root: return []
#         res=[]
#         def helper(root,ans,tmp):
#             if ans==0 and not root.left and not root.right:
#                 res.append(tmp)
#             if root.left:
#                 helper(root.left,ans-root.left.val,tmp+[root.left.val])
#             if root.right:
#                 helper(root.right,ans-root.right.val,tmp+[root.right.val])
#         helper(root,sum-root.val,[root.val])
#         return res

# @lc code=end
