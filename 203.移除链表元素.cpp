/*
 * @lc app=leetcode.cn id=203 lang=cpp
 *
 * [203] 移除链表元素
 *
 * https://leetcode-cn.com/problems/remove-linked-list-elements/description/
 *
 * algorithms
 * Easy (43.41%)
 * Likes:    332
 * Dislikes: 0
 * Total Accepted:    55.5K
 * Total Submissions: 127.2K
 * Testcase Example:  '[1,2,6,3,4,5,6]\n6'
 *
 * 删除链表中等于给定值 val 的所有节点。
 * 
 * 示例:
 * 
 * 输入: 1->2->6->3->4->5->6, val = 6
 * 输出: 1->2->3->4->5
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
class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode *last = head;
        while (last != nullptr && last->val == val)
        {
            last = last->next;
        }
        if (last == nullptr)
        {
            return nullptr;
        }
        ListNode *res = last;
        ListNode *cur = last->next;
        while (cur != nullptr)
        {
            if (cur->val == val)
            {
                last->next = cur->next;
                cur = cur->next;
            }
            else
            {
                last = cur;
                cur = cur->next;
            }
        }
        return res;
    }
};
// @lc code=end
