# [剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (root == nullptr) return ans;

        deque<TreeNode*> q;
        q.push_back(root);
        bool odd = true;
        while (!q.empty()) {
            int size = q.size();
            vector<int> tmp;
            for (int i = 0; i < size; i++) {
                TreeNode* curr = q.front(); q.pop_front();
                if (odd) tmp.push_back(curr->val);
                else tmp.insert(tmp.begin(), curr->val);
                if (curr->left) q.push_back(curr->left);
                if (curr->right) q.push_back(curr->right);
            }
            odd = !odd;
            ans.push_back(tmp);
        }

        return ans;
    }
};
```