# Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

 

**Example 1:**

![img](./assets/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**

```
Input: head = [1], n = 1
Output: []
```

**Example 3:**

```
Input: head = [1,2], n = 1
Output: [1]
```

 

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

 

**Follow up:** Could you do this in one pass?



Reflections:

- edge case when the first node is removed
- can consider moving the window of size n til the end



## Solution 1: two-pass

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # length - n nodes
        # edge case
        if length == n: return head.next

        curr = head
        for i in range(length - n - 1):
            curr = curr.next
        # remove nodes
        curr.next = curr.next.next
    
        return head
```

TC: O(n)

SC: O(1)

## Solution 2: one-pass

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        right = dummy
        for i in range(n):
            right = right.next
        left = dummy

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
```

TC: O(n)

SC: O(1)