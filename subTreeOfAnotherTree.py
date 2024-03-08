from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Naive solution using tree traversal
# Time complexity: O(m*n) where m is the number of nodes in the main tree and n is the number of nodes in the sub tree
class NaiveSolution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not (p and q):
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# Optimized solution using string comparison and hashing. Base on the idea of Merkle tree
class Solution:
    _PRE_CHAR = "#"
    _POST_CHAR = "$"
    _DELIMITER = ","
    _NULL_CHAR = "!"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First we build the string representation of the subtree (hash of it).
        # We can travel the tree in any order, but we need to keep the order consistent in both trees

        # We have to use special characters to represents:
        # - null nodes
        # - node values (to distinct between 2 nodes [2,2] and 1 node [22], for example)
        # - delimiters to separate the nodes

        subTreeHash = self.getSubTreeStrRepresentation(subRoot)

        # Then we traverse the main tree and compare the hash of the subtree with the hash of the main tree
        # If we find a match, we return True
        return self.travel(root, subTreeHash)[1]

    def getSubTreeStrRepresentation(self, node: Optional[TreeNode]) -> str:
        if not node:
            return str(hash(self._NULL_CHAR))

        return str(hash(self._PRE_CHAR + self.getSubTreeStrRepresentation(node.left) + self._DELIMITER + str(node.val) + self._DELIMITER + self.getSubTreeStrRepresentation(node.right) + self._POST_CHAR))

    def travel(self, node: Optional[TreeNode], target: str):
        if not node:
            return str(hash(self._NULL_CHAR)), str(hash(self._NULL_CHAR)) == target
        
        leftHash, cl = self.travel(node.left, target)
        if cl or leftHash == target:
            return leftHash, True

        rightHash, cr = self.travel(node.right, target)
        if cr or rightHash == target:
            return rightHash, True
        
        ch = str(hash(self._PRE_CHAR + leftHash + self._DELIMITER + str(node.val) + self._DELIMITER + rightHash + self._POST_CHAR))
        return ch, ch == target

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    print(solution.isSubtree(root, subRoot)) # True