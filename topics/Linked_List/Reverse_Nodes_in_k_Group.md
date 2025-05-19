# Reverse Nodes in k-Group

https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

**Example 1:**

![img](./assets/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

![img](./assets/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

 

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

 

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?



**Reflections**:

- when reverse group: we can set prev = groupNext to avoid breaking the linked list



## Solution 1: Iterative

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case
        if k == 1: return head
        
        groupPrev = dummy = ListNode(0, head)
        while True:
            # get kth node
            count = 0
            curr = groupPrev
            while curr and count < k:
                count += 1
                curr = curr.next
            kth = curr
            # if not kth: break
            if not kth: break

            groupNext = kth.next
            # reverse
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
```

TC: O(n)

SC: O(1)