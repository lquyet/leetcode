from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
``

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: 
            return None
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
    
def visualizeTree(root: Optional[TreeNode], space: int) -> None:
    if root is None:
        return
    space += 5
    visualizeTree(root.right, space)
    print()
    for i in range(5, space):
        print(end=" ")
    print(root.val)
    visualizeTree(root.left, space)
    
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    # write a function to visualize the binary tree
    visualizeTree(root, 0)
