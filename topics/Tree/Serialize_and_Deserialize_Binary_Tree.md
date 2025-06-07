# Serialize and Deserialize Binary Tree

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as [how LeetCode serializes a binary tree](https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode#h_01J5EGREAW3NAEJ14XC07GRW1A). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

**Example 1:**

![img](./assets/serdeser.jpg)

```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

**Example 2:**

```
Input: root = []
Output: []
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[0, 104]`.
- `-1000 <= Node.val <= 1000`

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```



**Reflections**:

- to build tree -> 
  - Dfs preorder
  - Bfs 
- There's no null node child for a null node: they will not be traversed or reconstruct
- Pay attention to the requirement of converting it to a string.



## Solution1: DFS Pre-order Recursive Top-down

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            # base case
            if not root: 
                res.append('N')
                return

            # preorder
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.index = 0
        def dfs():
            if vals[self.index] == "N": 
                self.index += 1
                return None
            root = TreeNode(int(vals[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

TC: O(N)

SC: O(N)



## Solution2: BFS

```python
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "N"

        res = []
        dq = deque([root])
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if node:
                    res.append(str(node.val))
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    res.append('N')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        if vals[0] == "N": return None
        root = TreeNode(int(vals[0]))
        dq = deque([root])

        index = 1
        while index < len(vals):
            node = dq.popleft()
            if vals[index] == "N": node.left = None
            else:
                node.left = TreeNode(int(vals[index]))
                dq.append(node.left)
            index += 1
            
            if vals[index] == "N": node.right = None
            else:
                node.right = TreeNode(int(vals[index]))
                dq.append(node.right)
            index += 1
            
        return root
```

TC: O(N)

SC: O(N)