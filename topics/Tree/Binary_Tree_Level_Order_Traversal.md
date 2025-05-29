# Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

 

**Example 1:**

![img](./assets/tree1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```
Input: root = []
Output: []
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`



## Solution (BFS)

```python
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        res = []
        
        while dq:
            n = len(dq)
            level = []
            for i in range(n):
                tmp = dq.popleft()
                level.append(tmp.val)
                if tmp.left:
                    dq.append(tmp.left)
                if tmp.right:
                    dq.append(tmp.right)
            res.append(level)
        return res
```

TC: O(n)

SC: O(n)