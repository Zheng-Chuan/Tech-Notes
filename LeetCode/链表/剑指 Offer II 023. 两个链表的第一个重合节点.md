# 剑指 Offer II 023. 两个链表的第一个重合节点
给定两个单链表的头节点 headA 和 headB ，请找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null

题目数据 保证 整个链式结构中不存在环

注意，函数返回结果后，链表必须 保持其原始结构

```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*> visited;
        ListNode* a = headA;
        while (a){
            visited.insert(a);
            a = a->next;
        }

        ListNode* b = headB;
        while (b){
            if (visited.count(b)) return b;
            b = b->next;
        }

        return nullptr;
    }
};
```