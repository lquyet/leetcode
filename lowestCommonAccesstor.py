# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# The (naive) idea solving this problem is we first travel the tree to find all parents of p -> store them in a set.
# We then travel the tree again to find q. Then we trace back q's parents. 
# Once we find a match between p's parents and q's parents, we return the match
# The time complexity of this solution is O(m + n) where m, n are the number of nodes in p and q, respectively
# Some possible optimizations:
# - The append operation in dfs may quite expensive. We can use a stack to store the parents instead, or pre-allocate the memory for the list.
# Remember that we must keep the order of parents in the FIRST travel. So we can't use a set to store p's parents. 
# - For q_parents, we can use a set instead (since we only use it for existence-check only) (but may have to modify the dfs function a little bit)

# UPDATED NOTE: I didn't realize the input tree is a BINARY SEARCH TREE. The following solution will work for any binary tree xD
# For binary search tree input, we have the following optimized solution.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_parents = []
        q_parents = []

        self.dfs(root, p, p_parents)
        self.dfs(root, q, q_parents)

        q_parents = set(q_parents)

        for parent in p_parents:
            if parent in q_parents:
                return parent
        
        return None


    def dfs(self, root: 'TreeNode', target: 'TreeNode', parents):
        if not root:
            return False
        
        if root == target:
            parents = parents.append(root)
            return True
        
        left = self.dfs(root.left, target, parents)
        if left:
            parents = parents.append(root)
            return True
        
        right = self.dfs(root.right, target, parents)
        if right:
            parents = parents.append(root)
            return True

        return False

class OptimizedSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return TreeNode(0)

if __name__ == "__main__":
    # Test cases
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left
    q = root.right

    print(Solution().lowestCommonAncestor(root, p, q).val) # Expected: 3

    p = root.left
    q = root.left.right

    print(Solution().lowestCommonAncestor(root, p, q).val) # Expected: 5