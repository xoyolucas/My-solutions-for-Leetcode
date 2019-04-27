#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
int maxDepth(TreeNode* root) {
    if(root==NULL)
        return 0;
    int left=maxDepth(root->left);
    int right=maxDepth(root->right);
    return (left>right)?(left+1):(right+1);
}

