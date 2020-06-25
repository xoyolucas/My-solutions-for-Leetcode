/*
 * @lc app=leetcode.cn id=257 lang=cpp
 *
 * [257] 二叉树的所有路径
 *
 * https://leetcode-cn.com/problems/binary-tree-paths/description/
 *
 * algorithms
 * Easy (64.09%)
 * Likes:    272
 * Dislikes: 0
 * Total Accepted:    41.1K
 * Total Submissions: 64.1K
 * Testcase Example:  '[1,2,3,null,5]'
 *
 * 给定一个二叉树，返回所有从根节点到叶子节点的路径。
 * 
 * 说明: 叶子节点是指没有子节点的节点。
 * 
 * 示例:
 * 
 * 输入:
 * 
 * ⁠  1
 * ⁠/   \
 * 2     3
 * ⁠\
 * ⁠ 5
 * 
 * 输出: ["1->2->5", "1->3"]
 * 
 * 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
#include <string>
using namespace std;

class Solution
{
public:
    vector<string> binaryTreePaths(TreeNode *root)
    {
        vector<string> res;
        string tmp = "";
        if (root == nullptr)
            return res;
        tmp += to_string(root->val);
        helper(root, res, tmp);
        return res;
    }

    void helper(TreeNode *root, vector<string> &res, string str)
    {
        if (root->left == nullptr && root->right == nullptr)
        {
            res.emplace_back(str);
        }
        if (root->left != nullptr)
        {
            helper(root->left, res, str + "->" + to_string(root->left->val));
        }
        if (root->right != nullptr)
        {
            helper(root->right, res, str + "->" + to_string(root->right->val));
        }
    }
};
// @lc code=end