# Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

 

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

 

**Constraints:**

- `k == lists.length`
- `0 <= k <= 104`
- `0 <= lists[i].length <= 500`
- `-104 <= lists[i][j] <= 104`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `104`.



**Reflections**:

- can speed up by grouping every two lists together (iterative merge sort)



## Solution

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # handle edge case
        if not lists: return None

        def merge(A, B):
            curr = dummy = ListNode()
            while A and B:
                if A.val < B.val:
                    curr.next = A
                    A, curr = A.next, curr.next
                else:
                    curr.next = B
                    B, curr = B.next, curr.next
            if A:
                curr.next = A
            if B:
                curr.next = B
            return dummy.next
        
        while len(lists) > 1:
            newList = []
            for i in range(0, len(lists), 2):
                if i + 1 == len(lists):
                    newList.append(merge(lists[i], None))
                else:
                    newList.append(merge(lists[i], lists[i+1]))
            lists = newList
        
        return lists[0]
```

TC: O(n log k)

SC: O(k)