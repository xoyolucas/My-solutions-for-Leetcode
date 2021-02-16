#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (59.52%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    77.3K
# Total Submissions: 129.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        left = head
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 左半部分
        pre.next = None
        # 右半部分反转
        right = self.reverse(slow)
        # 左半部分和反转的右半部分合并
        head = self.merge(left, right)
        return head

    def reverse(self, head):
        pre = None
        while head:
            nex = head.next
            head.next = pre
            pre = head
            head = nex

        return pre

    def merge(self, l1, l2):
        head = l1
        while l1 and l2:
            l1_next = l1.next
            l1.next = l2
            l1 = l2
            l2 = l1_next

        return head

# @lc code=end
