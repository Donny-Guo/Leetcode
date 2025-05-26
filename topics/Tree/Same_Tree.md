# Same Tree

https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

**Example 1:**

![img](./assets/ex1.jpg)

```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**

![img](./assets/ex2.jpg)

```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**

![img](./assets/ex3.jpg)

```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

 

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-104 <= Node.val <= 104`

---

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            # check self, left, right
            return (p.val == q.val 
                    and self.isSameTree(p.left, q.left) 
                    and self.isSameTree(p.right, q.right))
        else: # one is None, one is not None
            return False
```

TC: O(n)

SC: O(log n), O(n)

