/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > result;
        if(root==NULL)
            return result;
        queue<TreeNode*> node;
        node.push(root);
        while(!node.empty()){
            vector<int> tmp;
            int levelNum=node.size();   
            for(size_t i = 0; i < levelNum; ++i){
                if(node.front()->left!=NULL)
                    node.push(node.front()->left);
                if(node.front()->right!=NULL)
                    node.push(node.front()->right);
                tmp.push_back(node.front()->val);
                node.pop();
            }
            result.push_back(tmp);
        }
        return result;
    }
};