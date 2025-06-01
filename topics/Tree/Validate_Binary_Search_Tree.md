### Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/description/

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

 

**Example 1:**

![img](./assets/tree1-20250601010930162.jpg)

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

![img](./assets/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[1, 104]`.
- `-231 <= Node.val <= 231 - 1`



**Reflections**:

- Can do both top-down and bottom-up dfs
- bfs can also work: specify left and right limit correctly

---

## Solution: DFS Top-down

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if not root: return True

            if not left < root.val < right: return False

            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        
        return dfs(root, float('-inf'), float('inf'))
```

TC: O(N)

SC: O(N)



## Solution: DFS bottom-up

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left and not root.right: return [True, root.val, root.val]
            elif root.left and root.right:
                left = dfs(root.left)
                right = dfs(root.right)
                if left[0] and right[0] and left[2] < root.val < right[1]:
                    return [True, left[1], right[2]]
                else:
                    return [False, -1, -1]
            elif root.left:
                left = dfs(root.left)
                if left[0] and left[2] < root.val:
                    return [True, left[1], root.val]
                else:
                    return [False, -1, -1]
            else: # root.right is not empty
                right = dfs(root.right)
                if right[0] and right[1] > root.val:
                    return [True, root.val, right[2]]
                else:
                    return [False, -1, -1]
        return dfs(root)[0]
```

TC: O(N)

SC: O(N)