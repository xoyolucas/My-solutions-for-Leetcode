#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (66.78%)
# Likes:    752
# Dislikes: 0
# Total Accepted:    70.3K
# Total Submissions: 105.2K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
#
#
#
# 示例：
#
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
#
# 提示：
#
#
# 0 <= n <= 8
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def backTrace(begin, end):
            trees = []
            # 回溯终止条件
            # 左子树为空
            if begin > end:
                trees.append(None)
                return trees
            # 一个节点的树
            if begin == end:
                trees.append(TreeNode(begin))
                return trees

            # 以不同的值作为根节点
            for root_i in range(begin, end+1):
                # 所有可能的左子树
                leftTrees = backTrace(begin, root_i-1)
                # 所有可能的右子树
                rightTrees = backTrace(root_i+1, end)
                # 根节点与左右子树相连接
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        root = TreeNode(root_i)
                        root.left = leftTree
                        root.right = rightTree
                        trees.append(root)

            return trees

        if n == 0:
            return []
        return backTrace(1, n)

# @lc code=end