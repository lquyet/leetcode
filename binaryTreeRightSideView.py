from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The solution is quite simple as coded below. 
# Another approach is using BFS, we can list all nodes in each level and get the last node of each level.
# Both solutions have O(n) time complexity
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 1, res)

        return res

    
    def dfs(self, root: Optional[TreeNode], level: int, res: List[int]):
        if not root:
            return
        
        if level > len(res):
            res.append(root.val)
        
        self.dfs(root.right, level + 1, res)
        self.dfs(root.left, level + 1, res)

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(solution.rightSideView(root)) # [1, 3, 4]