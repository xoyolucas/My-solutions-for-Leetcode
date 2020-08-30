/*
 * @lc app=leetcode.cn id=543 lang=cpp
 *
 * [543] 二叉树的直径
 *
 * https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
 *
 * algorithms
 * Easy (50.48%)
 * Likes:    423
 * Dislikes: 0
 * Total Accepted:    62.1K
 * Total Submissions: 121.3K
 * Testcase Example:  '[1,2,3,4,5]'
 *
 * 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
 * 
 * 
 * 
 * 示例 :
 * 给定二叉树
 * 
 * ⁠         1
 * ⁠        / \
 * ⁠       2   3
 * ⁠      / \     
 * ⁠     4   5    
 * 
 * 
 * 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
 * 
 * 
 * 
 * 注意：两结点之间的路径长度是以它们之间边的数目表示。
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

#include <algorithm>
using namespace std;

class Solution
{
public:
    int diameterOfBinaryTree(TreeNode *root)
    {
        if (root == nullptr)
            return 0;

        int left_len = dfs(root->left) + 1;
        int right_len = dfs(root->right) + 1;

        return max(len, left_len + right_len);
    }

    int dfs(TreeNode *root)
    {
        if (root == nullptr)
            return -1;

        int left = 0;
        int right = 0;
        if (root->left)
            left = dfs(root->left) + 1;
        if (root->right)
            right = dfs(root->right) + 1;

        len = max(len, left + right);

        return max(left, right);
    }

private:
    int len{0}; // 保存当前直径
};
// @lc code=end
