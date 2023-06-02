# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case
            if root == None:
                return [True, 0]

            # General Case
            left_record = dfs(root.left)
            right_record = dfs(root.right)
            if left_record[0] == False or right_record[0] == False:
                balanced = False
            else:
                balanced = abs(left_record[1] - right_record[1]) <= 1
            height = max(left_record[1], right_record[1]) + 1
            return [balanced, height]
        return dfs(root)[0]