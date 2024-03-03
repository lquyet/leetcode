from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root: 
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return 0

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solution.maxDepth(root)) # 3
    
        