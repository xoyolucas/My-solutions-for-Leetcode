#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (44.10%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 58.8K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1
# board[i][j] 是一个小写英文字母
# 1
# 1
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
#
#
#

# @lc code=start
class TrieTreeNode(object):
    def __init__(self):
        self.end = False
        self.word = ''

        # The labels of pointers in the node
        self.pointerLabels = []

        # The pointers
        self.pointers = []


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(self, board, root, x, y):
            tmp = board[x][y]

            # 递归终止条件
            if tmp == '*' or tmp not in root.pointerLabels:
                return

            pos = root.pointerLabels.index(tmp)
            root = root.pointers[pos]
            if root.end:
                res.add(root.word)

            # 标记已访问
            board[x][y] = '*'
            if x+1 < rows:
                dfs(self, board, root, x+1, y)
            if y+1 < cols:
                dfs(self, board, root, x, y+1)
            if x > 0:
                dfs(self, board, root, x-1, y)
            if y > 0:
                dfs(self, board, root, x, y-1)
            # 恢复字符
            board[x][y] = tmp

        # 存储结果
        res = set()
        rows = len(board)
        cols = len(board[0]) if rows != 0 else 0
        if rows == 0 or cols == 0:
            return list(res)

        # 建立字典树Trie
        root = TrieTreeNode()
        for word in words:
            cur = root
            for i in range(len(word)):
                if word[i] not in cur.pointerLabels:
                    cur.pointerLabels.append(word[i])
                    newNode = TrieTreeNode()
                    cur.pointers.append(newNode)
                    cur = newNode

                # 字符在当前节点的子节点，且不为word的最后一位
                else:
                    pos = cur.pointerLabels.index(word[i])
                    cur = cur.pointers[pos]

                if i == len(word)-1:
                    cur.end = True
                    cur.word = word

        # dfs
        for i in range(rows):
            for j in range(cols):
                dfs(self, board, root, i, j)

        return list(res)
# @lc code=end
