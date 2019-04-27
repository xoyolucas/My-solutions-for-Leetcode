#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
void InOrderTraversal(TreeNode* root, vector<int>& v)
    {
        if(root->left)
            InOrderTraversal(root->left, v);
        v.push_back(root->val);
        if(root->right)
            InOrderTraversal(root->right, v);
        return;
    }

bool isValidBST(TreeNode* root) {
    vector<int> v;
    if(!root)
        return true;
    InOrderTraversal(root, v);
    for(int i=0; i<v.size()-1; i++)
        if(v[i] >= v[i+1])
            return false;
    return true;
}