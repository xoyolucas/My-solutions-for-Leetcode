/*
 * @lc app=leetcode.cn id=82 lang=cpp
 *
 * [82] 删除排序链表中的重复元素 II
 *
 * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
 *
 * algorithms
 * Medium (48.04%)
 * Likes:    299
 * Dislikes: 0
 * Total Accepted:    51K
 * Total Submissions: 106K
 * Testcase Example:  '[1,2,3,3,4,4,5]'
 *
 * 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
 * 
 * 示例 1:
 * 
 * 输入: 1->2->3->3->4->4->5
 * 输出: 1->2->5
 * 
 * 
 * 示例 2:
 * 
 * 输入: 1->1->1->2->3
 * 输出: 2->3
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
class Solution
{
public:
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }
        ListNode *new_head = new ListNode(0);
        ListNode *new_tail = new_head;
        int count = 0;
        while (head)
        {
            while (head && head->next && head->val == head->next->val)
            {
                count++;
                head = head->next;
            }
            if (count == 0)
            {
                new_tail->next = head;
                new_tail = new_tail->next;
            }
            count = 0;
            head = head->next;
        }
        new_tail->next = nullptr;

        return new_head->next;
    }
};
// @lc code=end
