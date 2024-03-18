from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""    
The idea is we calculate the max path sum in left and right subtree, combine it with root node value, and do that recursively. 
We can optimize the algorithm by somehow decrease the number of comparisons (which I think is quite redundant).
Time complexity: O(n), where n is the number of nodes in the binary tree
In each node, we do constant compare operations, so the time complexity is O(n)
After optimization, we can only reduce the number of constant compare operations, so the time complexity is still O(n)

Optimization:
In the code below, we do 9 comparisions before returning the value. While in fact, we only need to do 3:
- max(maxLeftPathSum, 0)
- max(maxRightPathSum, 0)
- max(maxLeftPathSum + maxRightPathSum + root.val, self._max_path_sum)

Because helper (and optimizedHelper) function always return the maxSum including the root node passed in the parameter,
and in each node, we do compare the maxSum of current step with global maxSum, therefore we don't need to worry about
the case when current node is not included in the maxSum path.
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._max_path_sum = float('-inf')
        # self.helper(root)
        self.optimizedHelper(root)
        return self._max_path_sum
    
    # helper return maxPathSumWithRoot
    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('-inf')

        maxLeftPathSum = self.helper(root.left)
        maxRightPathSum =  self.helper(root.right)

        if maxLeftPathSum != float('-inf'):
            self._max_path_sum = max(maxLeftPathSum, self._max_path_sum, maxLeftPathSum + root.val)
        
        if maxRightPathSum != float('-inf'):
            self._max_path_sum = max(maxRightPathSum, self._max_path_sum, maxRightPathSum + root.val)

        self._max_path_sum = max(self._max_path_sum, maxLeftPathSum + maxRightPathSum + root.val, root.val)

        return max(maxLeftPathSum, maxRightPathSum, 0) + root.val

    def optimizedHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxLeftPathSum = max(self.optimizedHelper(root.left), 0)
        maxRightPathSum = max(self.optimizedHelper(root.right), 0)

        self._max_path_sum = max(self._max_path_sum, maxLeftPathSum + maxRightPathSum + root.val)
        return max(maxLeftPathSum, maxRightPathSum, 0) + root.val

if __name__ == "__main__":
    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    solution = Solution()
    print(solution.maxPathSum(root1))  # Expected output: 6
    
    # Test case 2
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(solution.maxPathSum(root2))  # Expected output: 42
    
    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    print(solution.maxPathSum(root3))  # Expected output: 11

    # Test case 4
    root4 = TreeNode(-4)
    print(solution.maxPathSum(root4))  # Expected output: -4

        


