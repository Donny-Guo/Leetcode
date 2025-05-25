# Balanced Binary Tree

https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is **height-balanced**. (A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.)

 

**Example 1:**

![img](./assets/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**

![img](./assets/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**

```
Input: root = []
Output: true
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-104 <= Node.val <= 104`



## Solution

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> Tuple[int, bool]:
            # base case:
            if not root: return [0, True]

            # general case
            left = dfs(root.left)
            right = dfs(root.right)
            if not left[1] or not right[1]:
                return [-1, False]
            else:
                return (max(left[0], right[0]) + 1, abs(left[0]-right[0]) <= 1)
        
        return dfs(root)[1]
```

TC: O(n)

SC: worst case O(n)