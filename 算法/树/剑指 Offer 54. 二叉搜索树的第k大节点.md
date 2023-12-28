# [剑指 Offer 54. 二叉搜索树的第k大节点](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)

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
    int count = 0;
    int kthLargest(TreeNode* root, int k) {
        if (root == nullptr) return -1;

        int right_val = kthLargest(root->right, k);
        if (right_val != -1) {
            return right_val;
        }
            
        count++;
        if (count == k) {
            return root->val;
        } 

        int left_val = kthLargest(root->left, k);
        if (left_val != -1) {
            return left_val;
        }

        return -1;   
    }
};
```