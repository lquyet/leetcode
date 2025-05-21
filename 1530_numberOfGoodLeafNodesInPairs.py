class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Idea: at any node, we need the number of leafs in the left/right side + level of each leaf
# => uses a depth-first search (DFS) approach to traverse the binary tree 
# At each node, it recursively calculates the number of leaf nodes in the left and right subtrees.
# Then iterates over the possible distances between leaf nodes and calculates the number of valid pairs by multiplying the counts of leaf nodes in the left and right subtrees at each distance.
# Note that because we dfs in the left side first, therefore we loop for each appropriate levels in the right side. 
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if root is None:
                return {}

            left = dfs(root.left)
            right = dfs(root.right)

            if len(left) == 0 and len(right) == 0:
                return {1: 1}

            for ll in range(distance):
                rn = 0
                for lr in range(distance - ll + 1):
                    rn += right.get(lr, 0)
                res += left.get(ll, 0) * rn

            r = {}

            for level in range(distance):
                r[level+1] = left.get(level, 0) + right.get(level, 0)
            
            return r
        
        dfs(root)
        return res