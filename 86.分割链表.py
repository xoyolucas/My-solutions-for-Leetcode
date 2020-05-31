# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None or head.next == None:
            return head

        left = left_tmp = ListNode(0)
        right = right_tmp = ListNode(0)

        while head:
            if head.val < x:
                left_tmp.next = head
                left_tmp = left_tmp.next
            else:
                right_tmp.next = head
                right_tmp = right_tmp.next
            head = head.next

        # 小于X的尾连上大于等于X的头
        left_tmp.next = right.next
        # 大于等于X的尾指向None
        right_tmp.next = None

        return left.next
