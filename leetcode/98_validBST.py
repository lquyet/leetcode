from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The solution is quite simple, we manage the minimum and maximum values of the subtrees and check if the current node is within the range of the minimum and maximum values of the subtrees.
# Another solution I found on leetcode is that we can use inorder traversal (which will output the elements in ascending order) and check if there are any 2 consecutive elements not following that order.
# Yet another solution is we can simplify the dfs function. There is no need to keep track of the minimun and maximum values of the subtrees. 
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, check = self.dfs(root)
        return check

    def dfs(self, root: 'TreeNode'):
        if not root:
            return float('inf'), float('-inf'), True
        
        min_left, max_left, left_check = self.dfs(root.left)
        if not left_check:
            return 0, 0, False

        min_right, max_right, right_check = self.dfs(root.right)
        if not right_check:
            return 0, 0, False
        
        if max_left >= root.val:
            return 0, 0, False
        
        if min_right <= root.val:
            return 0, 0, False
        
        min_val = min(min_left, root.val, min_right)
        max_val = max(max_left, root.val, max_right)

        return min_val, max_val, True
    
class OptimizedSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, left_limit, right_limit):
            print("left_limit: ", left_limit, "right_limit: ", right_limit)
            if node is None:
                return True
            if not (left_limit < node.val < right_limit):
                return False
            return validate(node.left, left_limit, node.val) and validate(node.right, node.val, right_limit)

        if root == None:
            return True

        return validate(root.left, float("-inf"), root.val) and validate(root.right, root.val, float("inf"))


if __name__ == "__main__":
    # Test case 1: Valid BST
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   2   4   8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    print(Solution().isValidBST(root))  # Output: True

    # Test case 2: Invalid BST
    #       5
    #      / \
    #     3   7
    #    / \   \
    #   2   6   8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(8)
    print(Solution().isValidBST(root))  # Output: False

    # Test case 3: Empty tree
    root = None
    print(Solution().isValidBST(root))  # Output: True

    
