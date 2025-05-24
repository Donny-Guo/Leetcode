# Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

 

**Example 1:**

![img](./assets/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-100 <= Node.val <= 100`

---

## Solution (DFS)

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            # base case
            if not root: return 0

            # general case
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            self.res = max(self.res, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return self.res

```

TC: O(n)

SC: worst case O(n), best case O(log n) (balanced tree)