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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not (p and q):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
