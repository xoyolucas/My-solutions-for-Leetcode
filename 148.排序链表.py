#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (65.81%)
# Likes:    672
# Dislikes: 0
# Total Accepted:    80.7K
# Total Submissions: 121.4K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        root, length = head, 0
        size = 1  # 子数组大小
        while root:
            root, length = root.next, length + 1

        res = ListNode(0)
        res.next = head
        while size < length:
            new_head = res.next
            prev = res
            while new_head:
                h1 = new_head
                i = size
                while new_head and i:
                    new_head = new_head.next
                    i -= 1
                if i != 0:  # no need to merge because the `h2` is None.
                    break

                h2 = new_head
                i = size
                while new_head and i:
                    new_head = new_head.next
                    i -= 1

                count1 = size
                count2 = size - i

                # merge
                while count1 and count2:
                    if h1.val < h2.val:
                        prev.next, h1 = h1, h1.next
                        count1 -= 1
                    else:
                        prev.next, h2 = h2, h2.next
                        count2 -= 1
                    prev = prev.next
                while count1 > 0:
                    prev.next, h1 = h1, h1.next
                    count1 -= 1
                    prev = prev.next
                while count2 > 0:
                    prev.next, h2 = h2, h2.next
                    count2 -= 1
                    prev = prev.next
                prev.next = new_head #合并后的子串next指向还未合并的头部

            size *= 2  # 子串长度翻倍

        return res.next


# @lc code=end

