/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 *
 * https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
 *
 * algorithms
 * Medium (63.65%)
 * Likes:    416
 * Dislikes: 0
 * Total Accepted:    71.6K
 * Total Submissions: 111.4K
 * Testcase Example:  '[1,2,3,4]'
 *
 * 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
 * 
 * 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 * 
 * 
 * 
 * 示例:
 * 
 * 给定 1->2->3->4, 你应该返回 2->1->4->3.
 * 
 * 
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <list>
using namespace std;

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }

        ListNode *res = head->next;
        ListNode *prev = new ListNode(0);

        while (head != nullptr && head->next != nullptr)
        {
            ListNode *first = head;
            ListNode *second = head->next;

            prev->next = second;
            first->next = second->next;
            second->next = first;

            prev = first;
            head = first->next;
        }
        return res;
    }
};
// @lc code=end
// 递归
// class Solution(object):
//     def swapPairs(self, head: ListNode) -> ListNode:
//         """
//         :type head: ListNode
//         :rtype: ListNode
//         """

//         # If the list has no node or has only one node left.
//         if not head or not head.next:
//             return head

//         # Nodes to be swapped
//         first_node = head
//         second_node = head.next

//         # Swapping
//         first_node.next  = self.swapPairs(second_node.next)
//         second_node.next = first_node

//         # Now the head is the second node
//         return second_node
