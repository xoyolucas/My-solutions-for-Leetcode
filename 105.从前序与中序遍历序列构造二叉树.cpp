/*
 * @lc app=leetcode.cn id=105 lang=cpp
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (67.29%)
 * Likes:    607
 * Dislikes: 0
 * Total Accepted:    102.3K
 * Total Submissions: 151.2K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 根据一棵树的前序遍历与中序遍历构造二叉树。
 * 
 * 注意:
 * 你可以假设树中没有重复的元素。
 * 
 * 例如，给出
 * 
 * 前序遍历 preorder = [3,9,20,15,7]
 * 中序遍历 inorder = [9,3,15,20,7]
 * 
 * 返回如下的二叉树：
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
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
#include <unordered_map>
using namespace std;

class Solution
{
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        int pre_len = preorder.size();
        int in_len = inorder.size();
        if (pre_len == 0 || in_len == 0 || pre_len != in_len)
            return nullptr;
        unordered_map<int, int> inorder_map;
        for (int i = 0; i < in_len; i++)
        {
            inorder_map[inorder[i]] = i;
        }

        return buildTree(preorder, 0, pre_len - 1, 0, in_len - 1, inorder_map);
    }

    TreeNode *buildTree(vector<int> &preorder, int pre_left, int pre_right, int in_left,
                        int in_right, unordered_map<int, int> &inorder_map)
    {
        if (pre_left > pre_right || in_left > in_right)
            return nullptr;

        int val = preorder[pre_left];
        TreeNode *root = new TreeNode(val);
        root->left = buildTree(preorder, pre_left + 1, inorder_map[val] - in_left + pre_left,
                               in_left, inorder_map[val] - 1, inorder_map);

        root->right = buildTree(preorder, inorder_map[val] - in_left + pre_left + 1, pre_right,
                                inorder_map[val] + 1, in_right, inorder_map);

        return root;
    }
};
// @lc code=end
