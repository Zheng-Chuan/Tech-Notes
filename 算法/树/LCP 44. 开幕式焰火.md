# [LCP 44. 开幕式焰火](https://leetcode.cn/problems/sZ59z6/)

```c++
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
    set<int> colors;
    int numColor(TreeNode* root) {
        helper(root);
        return colors.size();        
    }

    void helper(TreeNode* root) {
        if (root == nullptr) return;

        colors.insert(root->val);
        helper(root->left);
        helper(root->right);
    }
};

```