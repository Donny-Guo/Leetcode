### Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given the `root` of a binary search tree, and an integer `k`, return *the* `kth` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

 

**Example 1:**

![img](./assets/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**

![img](./assets/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

 

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 104`
- `0 <= Node.val <= 104`

 

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?



**Reflections**:

- In-order traversal:
  - recursion dfs: (need a nonlocal variable for count if we want to stop as soon as we hit the kth node)
  - iterative dfs (stack + curr ptr): go as left as possible, pushing to stack; pop the stack and move curr ptr to the right of popped node



## Solution 1 (DFS recursive)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      count = 0
      res = root.val
      def dfs(node):
        if not node: return
      	nonlocal count, res
      	dfs(node.left)
        count += 1
        if count == k: res = node.val
        dfs(node.right)
      dfs(root)
      return res
```

TC: O(N)

SC: O(N)



## Solution (DFS iterative)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        curr = root

        while stack or curr:
            # append all left nodes of curr
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # pop
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
```

TC: O(N)

SC: O(N)