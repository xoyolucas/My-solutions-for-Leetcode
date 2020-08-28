#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (54.04%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    72K
# Total Submissions: 133.2K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
#
#
#
# 提示：
#
#
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
#
#
#

# 将当前搜索的节点 u 标记为「搜索中」，遍历该节点的每一个相邻节点 v：
# 状态0：如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；
# 状态1：如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
# 状态2：如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，
# 因此 u 无论何时入栈都不会影响到 (u, v) 之前的拓扑关系，以及不用进行任何操作。
# 当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。
# 拓扑排序

# @lc code=start
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = collections.defaultdict(list)
        visited = [0]*numCourses
        valid = True

        # 构造拓扑
        for next, pre in prerequisites:
            adjacency[pre].append(next)

        def dfs(root):
            nonlocal valid
            visited[root] = 1
            for child in adjacency[root]:
                if visited[child] == 1:
                    valid = False
                    return
                elif visited[child] == 0:
                    dfs(child)
                    if not valid:
                        return
            visited[root] = 2

        for i in range(numCourses):
            if visited[i] == 0 and valid:
                dfs(i)
        return valid

# @lc code=end