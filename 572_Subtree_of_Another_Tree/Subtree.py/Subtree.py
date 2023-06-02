# Understand
# Input: two roots: root and subRoot
# Output: bool:  whether the subRoot is the subtree of root
# Example:
#  1. root and subRoot are the same -->True
#  2. 

# Match:
# 1. same tree problem
# 2. recursion

# Plan 
# 1. write the function to find the same tree
#   1. base case: root1 and root2 are both None
#                 root1 is None  OR root2 is None
#   2. general case:
#               compare root1.val and root2.val
#               recursion call: left and right
#               return value
# 2. base case: root1 and root2 are both None
#               root1 is None  OR root2 is None
# 3. general case:
#               compare itself
#               compare left and right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            # Base case
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False

            # General case
            return (p.val == q.val) and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        # Base case:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        # General case:
        if isSameTree(root, subRoot):
            return True
        
        return ( self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) )