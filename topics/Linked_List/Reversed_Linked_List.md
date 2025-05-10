### Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/description/

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

 

**Example 1:**

![img](./assets/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

![img](./assets/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

 

**Constraints:**

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?



## Solution - Iterative

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
```

TC: O(n)

SC: O(1)

## Solution - Recursive

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive

        # base case
        if not head or head.next == None:
            return head

        # general case
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
```

TC: O(n)

SC: O(m) for call stack