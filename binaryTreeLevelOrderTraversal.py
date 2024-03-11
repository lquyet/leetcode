from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The idea is quite simple. We do bfs and keep track of the level of each node.
# We can also use recursion to solve this problem by calling the recursive function like recur(root.left, level + 1)... . But the iterative solution is more efficient.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)]
        res = []

        while len(queue) > 0:
            node, level = queue.pop(0)

            if node:
                if level == len(res):
                    res.append([])

                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        return res
    
if __name__ == "__main__":
    # Test cases
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrder(root)) # Expected: [[3], [9, 20], [15, 7]]

