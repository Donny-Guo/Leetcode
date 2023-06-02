# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion method: 
# O(n) time complexity because every node needs to be visited
# O(n) space complexity because the worst case there will be n function call placed in the stack
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Input: root of binary tree
        # Output: return the root of the inverted tree
        
        # Match:
        # 1. recursion
        
        # Plan:
        # 1. base case: if root is None, return;if two children are None, return;  
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None
        # 2. general case: switch two children
        #   1. invert left child
        root.left = self.invertTree(root.left)
        #.  2. invert right child
        root.roght = self.invertTree(root.right)
        #.  3. invert left and right child
        (root.left, root.right) = (root.right, root.left)
        return root


        
