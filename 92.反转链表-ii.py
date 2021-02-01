#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.99%)
# Likes:    636
# Dislikes: 0
# Total Accepted:    95.5K
# Total Submissions: 183.7K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 第一次反转：1(head) 2(next) 3 4 5 反转为 2 1 3 4 5
    # 第二次反转：2 1(head) 3(next) 4 5 反转为 3 2 1 4 5
    # 第三次发转：3 2 1(head) 4(next) 5 反转为 4 3 2 1 5
    # 第四次反转：4 3 2 1(head) 5(next) 反转为 5 4 3 2 1
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre = dummy_head

        # 寻找反转起始位置的pre节点
        for i in range(m-1):
            pre = pre.next

        left = pre.next
        for _ in range(m, n):
            right = left.next
            left.next = right.next
            right.next = pre.next
            pre.next = right

        return dummy_head.next
# @lc code=end
