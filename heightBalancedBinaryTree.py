from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         self.isBalanced = True
#         self.dfs(root)
#         return self.isBalanced

    
#     def dfs(self, root: Optional[TreeNode]):
#         if not root:
#             return 0
        
#         if not self.isBalanced:
#             return 0
        
#         left = self.dfs(root.left)
#         right = self.dfs(root.right)

#         if abs(left - right) > 1:
#             self.isBalanced = False
        
#         return max(left, right) + 1
        
# Optimized solution: Reduce the number of times we call the dfs function by returning immediately if the tree is not balanced
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, c = self.dfs(root)
        return c

    
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0, True
        
        left, cl = self.dfs(root.left)
        if not cl:
            return 0, False
        right, cr = self.dfs(root.right)
        if not cr: 
            return 0, False

        if abs(left - right) > 1:
            return 0, False
        
        return max(left, right) + 1, True