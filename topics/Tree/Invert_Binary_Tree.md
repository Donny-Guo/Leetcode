# Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/description/

Given the `root` of a binary tree, invert the tree, and return *its root*.

 

**Example 1:**

![img](./assets/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2:**

![img](./assets/invert2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3:**

```
Input: root = []
Output: []
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`



## Solution

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root: return None

        # general case
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root
```

TC: O(n) (go through every node)

SC: O(n) (worst case: consider all nodes only have left child)