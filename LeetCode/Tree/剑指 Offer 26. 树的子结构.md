# [剑指 Offer 26. 树的子结构](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def helper(A, B):
            if not A: return False
            sub = False
            if A.val == B.val: sub = isSub(A, B)
            return helper(A.left, B) or helper(A.right, B) or sub

        def isSub(A, B):
            if not A and not B: 
                return True
            if A and not B: 
                return True
            if B and not A: 
                return False
            if A.val != B.val: 
                return False
            else:
                return isSub(A.left, B.left) and isSub(A.right, B.right)

        if not B: return False
        return helper(A, B)
```