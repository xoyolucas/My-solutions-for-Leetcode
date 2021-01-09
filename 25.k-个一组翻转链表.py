#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (63.71%)
# Likes:    829
# Dislikes: 0
# Total Accepted:    123K
# Total Submissions: 192.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
# 说明：
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 翻转链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        cur = head
        while prev != tail:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pseudo_head = ListNode(0)
        pseudo_head.next = head

        pre = pseudo_head

        while head:
            tail = pre

            for _ in range(k):
                # 向前进k个元素
                tail = tail.next
                # 若不足k个，则返回头结点
                if not tail:
                    return pseudo_head.next

            new_head = tail.next
            head, tail = self.reverse(head, tail)
            # 与翻转后的子链表连接
            pre.next = head
            tail.next = new_head
            pre = tail
            head = new_head

        return pseudo_head.next

# @lc code=end
