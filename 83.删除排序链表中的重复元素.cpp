/*
 * @lc app=leetcode.cn id=83 lang=cpp
 *
 * [83] 删除排序链表中的重复元素
 *
 * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
 *
 * algorithms
 * Easy (49.74%)
 * Likes:    281
 * Dislikes: 0
 * Total Accepted:    86.8K
 * Total Submissions: 174.6K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
 * 
 * 示例 1:
 * 
 * 输入: 1->1->2
 * 输出: 1->2
 * 
 * 
 * 示例 2:
 * 
 * 输入: 1->1->2->3->3
 * 输出: 1->2->3
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
        auto *p = head;

        while (p != nullptr && p->next != nullptr)
        {
            if (p->val == p->next->val)
            {
                // auto *tmp=p->next;
                // delete tmp;
                // tmp=nullptr;
                p->next = p->next->next;
            }
            else
            {
                p = p->next;
            }
        }

        return head;
    }
};
// @lc code=end