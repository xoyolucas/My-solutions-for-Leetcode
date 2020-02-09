/*
 * @lc app=leetcode.cn id=501 lang=cpp
 *
 * [501] 二叉搜索树中的众数
 *
 * https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
 *
 * algorithms
 * Easy (43.20%)
 * Likes:    76
 * Dislikes: 0
 * Total Accepted:    8.3K
 * Total Submissions: 19K
 * Testcase Example:  '[1,null,2,2]'
 *
 * 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
 * 
 * 假定 BST 有如下定义：
 * 
 * 
 * 结点左子树中所含结点的值小于等于当前结点的值
 * 结点右子树中所含结点的值大于等于当前结点的值
 * 左子树和右子树都是二叉搜索树
 * 
 * 
 * 例如：
 * 给定 BST [1,null,2,2],
 * 
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  2
 * 
 * 
 * 返回[2].
 * 
 * 提示：如果众数超过1个，不需考虑输出顺序
 * 
 * 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
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
    vector<int> findMode(TreeNode *root)
    {
        vector<int> res;
        if (root != nullptr)
        {
            TreeNode *pre = nullptr;
            int cur_times = 1; //第一个元素的pre为nullptr
            int max_times = 0;
            orderSearch(root, pre, cur_times, max_times, res);
        }

        return res;
    }

    void orderSearch(TreeNode *root, TreeNode *&pre, int &cur_times, int &max_times, vector<int> &res)
    {
        if (root == nullptr)
            return;
        orderSearch(root->left, pre, cur_times, max_times, res);
        if (pre != nullptr)
        {
            cur_times = (root->val == pre->val) ? cur_times + 1 : 1;
        }
        if (cur_times == max_times)
        {
            res.push_back(root->val);
        }
        else if (cur_times > max_times)
        {
            max_times = cur_times;
            res.clear();
            res.push_back(root->val);
        }
        pre = root;
        orderSearch(root->right, pre, cur_times, max_times, res);
    }
};

// 二叉搜索树的中序遍历是一个升序序列，逐个比对当前结点(root)值与前驱结点（pre)值。
// 更新当前节点值出现次数(curTimes)及最大出现次数(maxTimes);
// 更新规则：若curTimes=maxTimes,将root->val添加到结果向量(res)中；
// 若curTimes>maxTimes,清空res,将root->val添加到res,并更新maxTimes为curTimes。
// class Solution:
//     def __init__(self):
//         self.res={}
//     def findMode(self, root: TreeNode) -> List[int]:
//         result=[]
//         if root==None:
//             return []
//         self.visit(root)
//         Max=max(self.res.values())
//         for key in self.res:
//             if self.res[key]==Max:
//                 result.append(key)
//         return result


    
//     def visit(self,root):
//         if root:
//             self.res[root.val]=self.res.get(root.val,0)+1
//             self.visit(root.left)
//             self.visit(root.right)
// @lc code=end
