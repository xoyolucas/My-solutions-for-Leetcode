#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode-cn.com/problems/task-scheduler/description/
#
# algorithms
# Medium (50.54%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    30.4K
# Total Submissions: 60K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26
# 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的最短时间。
#
#
#
# 示例 ：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# ⁠    在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
#
#
#
# 提示：
#
#
# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。
#
#
#

# @lc code=start


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)
        if size <= 1:
            return size

        # 统计task的数量
        task_map = {}
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        
        # 按value进行排序
        task_map = sorted(task_map.items(),key=lambda x: x[1], reverse=True)

        max_count = task_map[0][1]
        min_total_count = (max_count-1)*(n+1)

        for task in task_map:
            if task[1] == max_count:
                min_total_count += 1
            else:
                break

        return min_total_count if min_total_count > size else size

# @lc code=end