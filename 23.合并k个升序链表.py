#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (53.17%)
# Likes:    911
# Dislikes: 0
# Total Accepted:    170.9K
# Total Submissions: 321.5K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        for index, node in enumerate(lists):
            # 将当前头结点的value以及该头结点所在的链表index入堆
            if node != None:
                heappush(min_heap, (node.val, index))

        head = ListNode(-1)
        cur = head
        while len(min_heap) != 0:
            val, index = heappop(min_heap)
            # 取出最小的元素加入到合并链表中
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            # 将新的头结点加入到最小堆中
            if lists[index] != None:
                heappush(min_heap, (lists[index].val, index))

        return head.next
# @lc code=end
