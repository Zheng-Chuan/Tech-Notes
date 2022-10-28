# [剑指 Offer 32 - I. 从上到下打印二叉树](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

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
    vector<int> levelOrder(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) return res;

        deque<TreeNode*> q;
        q.push_back(root);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* curr = q.front(); q.pop_front();
                res.push_back(curr->val);
                if (curr->left) q.push_back(curr->left);
                if (curr->right) q.push_back(curr->right);
            }
        }

        return res;
    }
};
```