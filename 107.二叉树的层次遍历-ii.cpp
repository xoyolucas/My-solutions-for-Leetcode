/*
 * @lc app=leetcode.cn id=107 lang=cpp
 *
 * [107] 二叉树的层次遍历 II
 *
 * https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
 *
 * algorithms
 * Easy (64.70%)
 * Likes:    214
 * Dislikes: 0
 * Total Accepted:    49.6K
 * Total Submissions: 76.7K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
 * 
 * 例如：
 * 给定二叉树 [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 返回其自底向上的层次遍历为：
 * 
 * [
 * ⁠ [15,7],
 * ⁠ [9,20],
 * ⁠ [3]
 * ]
 * 
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

class Solution
{
public:
    vector<vector<int>> levelOrderBottom(TreeNode *root)
    {
        vector<vector<int>> res;
        vector<TreeNode *> first;
        vector<TreeNode *> second;
        vector<int> level;

        if (root == nullptr)
        {
            return res;
        }

        first.push_back(root);
        
        int index = 0;
        while (index < first.size())
        {
            TreeNode *head = first[index];
            level.push_back(head->val);

            if (head->left != nullptr)
            {
                second.push_back(head->left);
            }
            if (head->right != nullptr)
            {
                second.push_back(head->right);
            }

            if (index == first.size() - 1)
            {
                first.clear();
                first = second;
                res.push_back(level);
                level.clear();
                second.clear();
                index = 0;
            }
            else
            {
                index++;
            }
        }

        reverse(res.begin(), res.end());

        return res;
    }
};
// @lc code=end