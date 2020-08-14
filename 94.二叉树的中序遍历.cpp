/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Medium (72.28%)
 * Likes:    600
 * Dislikes: 0
 * Total Accepted:    205.6K
 * Total Submissions: 284.2K
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树，返回它的中序 遍历。
 * 
 * 示例:
 * 
 * 输入: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 * 
 * 输出: [1,3,2]
 * 
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <vector>
#include <stack>
using namespace std;

class Solution
{
public:
    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> ans;
        stack<TreeNode *> tmp;
        if (root == nullptr)
            return ans;

        TreeNode *cur = root;
        while (cur != nullptr || !tmp.empty())
        {
            while (cur != nullptr)
            {
                tmp.push(cur);
                cur = cur->left;
            }

            TreeNode *top = tmp.top();
            tmp.pop();
            ans.push_back(top->val);
            cur = top->right;
        }
        return ans;
    }
};
// @lc code=end