# [剑指 Offer II 045. 二叉树最底层最左边的值](https://leetcode.cn/problems/LwUNpT/)

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        deque<TreeNode*> q;
        q.push_back(root);
        int ans = root->val;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* curr = q.front(); q.pop_front();
                if (curr->right) 
                    q.push_back(curr->right);
                if (curr->left) 
                    q.push_back(curr->left);
            }
            ans = q.back()->val;
        }
        return ans;
    }
};
```