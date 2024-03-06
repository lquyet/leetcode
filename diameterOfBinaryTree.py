from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.travel(root)
        return self.diameter
    
    def travel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.travel(root.left)
        right = self.travel(root.right)
        current_diameter = left + right
        self.diameter = max(self.diameter, current_diameter)

        return max(left, right) + 1

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(solution.diameterOfBinaryTree(root)) # 3

        