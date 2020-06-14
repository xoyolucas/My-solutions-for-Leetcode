/*
 * @lc app=leetcode.cn id=144 lang=cpp
 *
 * [144] 二叉树的前序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Medium (65.77%)
 * Likes:    279
 * Dislikes: 0
 * Total Accepted:    115.1K
 * Total Submissions: 174.9K
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树，返回它的 前序 遍历。
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
 * 输出: [1,2,3]
 * 
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
using namespace std;

class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> res;
        helper(root, res);
        return res;
    }

    void helper(TreeNode *root, vector<int> &res)
    {
        if (root == nullptr)
        {
            return;
        }

        res.emplace_back(root->val);
        helper(root->left, res);
        helper(root->right, res);
    }
};

// iterate, use stack to imitate recursive
// vector<int> preorderTraversal(TreeNode* root) {
//     vector<int> v;
//     if(!root) return v;
//     TreeNode* temp = root;
//     stack<TreeNode*> s;
//     s.push(root);
//     while(!s.empty()){
//         temp = s.top();
//         s.pop();
//         v.push_back(temp->val);
//         if(temp->right) s.push(temp->right);
//         if(temp->left) s.push(temp->left);
//     }
// }
// @lc code=end
