#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (43.99%)
# Likes:    554
# Dislikes: 0
# Total Accepted:    71K
# Total Submissions: 159.5K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#
#

# @lc code=start
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addNode(word):
            nonlocal node_num
            if word not in word2id:
                word2id[word] = node_num
                node_num += 1

        def addEdge(word):
            addNode(word)
            id1 = word2id[word]
            # 创建虚拟节点与原本的节点相连接
            for i in range(len(word)):
                tmp = word[:i]+'*'+word[i+1:]
                addNode(tmp)
                id2 = word2id[tmp]
                edge[id1].append(id2)
                edge[id2].append(id1)

        word2id = {}
        edge = collections.defaultdict(list)

        node_num = 0
        for word in wordList:
            addEdge(word)
        addEdge(beginWord)

        # 宿节点不在字典中
        if endWord not in wordList:
            return 0

        # 双向BFS
        dis_forward = [float('inf')] * node_num
        begin_id = word2id[beginWord]
        dis_forward[begin_id] = 0
        queue_forward = collections.deque([begin_id])

        dis_backward = [float('inf')] * node_num
        end_id = word2id[endWord]
        dis_backward[end_id] = 0
        queue_backward = collections.deque([end_id])

        while queue_forward and queue_backward:
            # 正向广度优先搜索
            for _ in range(len(queue_forward)):
                node = queue_forward.popleft()
                # 正反向相遇
                if dis_backward[node] != float('inf'):
                    return (dis_forward[node]+dis_backward[node])//2+1
                for neighbor in edge[node]:
                    if dis_forward[neighbor] == float("inf"):
                        dis_forward[neighbor] = dis_forward[node] + 1
                        queue_forward.append(neighbor)

            # 反向广度优先搜索
            for _ in range(len(queue_backward)):
                node = queue_backward.popleft()
                # 正反向相遇
                if dis_forward[node] != float('inf'):
                    return (dis_forward[node]+dis_backward[node])//2+1
                for neighbor in edge[node]:
                    if dis_backward[neighbor] == float("inf"):
                        dis_backward[neighbor] = dis_backward[node] + 1
                        queue_backward.append(neighbor)

        return 0
# @lc code=end
