from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The idea is we gonna travel through the tree in-order, which results in a sorted array.
# We then just need to return the k-th element of that array. 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self._k = k
        self._total_calls = 0
        self.in_order(root)
        print(f"Total calls: {self._total_calls}")
        return self.res[k-1]

        
    def in_order(self, root: Optional[TreeNode]):
        if len(self.res) >= self._k or not root:
            return 
        
        self.in_order(root.left)
        self.res.append(root.val)
        self.in_order(root.right)

# Another faster solution is to use a stack to simulate the in-order traversal.
# We first push all the left nodes into the stack, then we pop the top element and push its right node into the stack.
class OptimizedSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while True:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right


if __name__ == "__main__":
    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1
    solution = OptimizedSolution()
    result = solution.kthSmallest(root, k)
    print(f"Test case 1: {result}")  # Expected output: 1

    # Test case 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    solution = OptimizedSolution()
    result = solution.kthSmallest(root, k)
    print(f"Test case 2: {result}")  # Expected output: 3

    # Test case 3
    root = TreeNode(1)
    k = 1
    solution = OptimizedSolution()
    result = solution.kthSmallest(root, k)
    print(f"Test case 3: {result}")  # Expected output: 1