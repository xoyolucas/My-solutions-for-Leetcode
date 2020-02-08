/*
 * @lc app=leetcode.cn id=437 lang=cpp
 *
 * [437] 路径总和 III
 *
 * https://leetcode-cn.com/problems/path-sum-iii/description/
 *
 * algorithms
 * Easy (53.22%)
 * Likes:    276
 * Dislikes: 0
 * Total Accepted:    19.4K
 * Total Submissions: 36.2K
 * Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
 *
 * 给定一个二叉树，它的每个结点都存放着一个整数值。
 * 
 * 找出路径和等于给定数值的路径总数。
 * 
 * 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
 * 
 * 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
 * 
 * 示例：
 * 
 * root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
 * 
 * ⁠     10
 * ⁠    /  \
 * ⁠   5   -3
 * ⁠  / \    \
 * ⁠ 3   2   11
 * ⁠/ \   \
 * 3  -2   1
 * 
 * 返回 3。和等于 8 的路径有:
 * 
 * 1.  5 -> 3
 * 2.  5 -> 2 -> 1
 * 3.  -3 -> 11
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
    int pathSum(TreeNode *root, int sum)
    {
        vector<int> vec(1000, 0);
        return helper(root, sum, vec, 0);
    }

    int helper(TreeNode *root, int sum, vector<int> vec, int p)
    {
        if (root == nullptr)
            return 0;
        vec[p] = root->val;
        int count = 0;
        int tmp = 0;
        for (int i = p; i >= 0; --i)
        {
            tmp += vec[i];
            if (tmp == sum)
            {
                ++count;
            }
        }

        return count + helper(root->left, sum, vec, p + 1) + helper(root->right, sum, vec, p + 1);
    }
};

// int pathSum(TreeNode *rt, int sum)
// {
//     unordered_map<int, int> cnt{{0, 1}};
//     return helper(rt, sum, cnt, 0);
// }
// int helper(TreeNode *rt, int sum, unordered_map<int, int> &cnt, int pre)
// {
//     if (!rt)
//         return 0;
//     pre += rt->val;
//     int ans = cnt[pre - sum];
//     ++cnt[pre];
//     ans += helper(rt->left, sum, cnt, pre) + helper(rt->right, sum, cnt, pre);
//     --cnt[pre];
//     return ans;
// };
// @lc code=end
