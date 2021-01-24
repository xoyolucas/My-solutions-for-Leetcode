# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 判断第k个节点是否存在
        # 如果第 k 个节点位于第 h 层，则 k 的二进制表示包含 h+1 位，其中最高位是 1，
        # 其余各位从高到低表示从根节点到第 k 个节点的路径，0 表示移动到左子节点，11 表示移动到右子节点。
        # 通过位运算得到第 k 个节点对应的路径，判断该路径对应的节点是否存在，即可判断第 k 个节点是否存在。
        def exist(root, level, k):
            mask = 1 << (level - 1)
            node = root
            while node and mask > 0:
                if mask & k:
                    node = node.right
                else:
                    node = node.left
                mask >>= 1

            return node != None

        if not root:
            return 0

        level = -1
        cur = root
        # 判断层数
        while cur:
            level += 1
            cur = cur.left
    
        low = 1 << level
        high = (1 << (level + 1)) - 1
        print(low,high)
        # 二分查找
        while low < high:
            mid = (high - low + 1) // 2 + low
            if exist(root, level, mid):
                low = mid
            else:
                high = mid - 1

        return low

