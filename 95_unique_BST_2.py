from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def createBstRange(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            
            if start == end:
                root = TreeNode(start)
                return [root]
            
            for i in range(start, end+1):
                leftSubtree = createBstRange(start, i-1)
                rightSubtree = createBstRange(i+1, end)

                for l in leftSubtree:
                    for r in rightSubtree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            
            return res


        return createBstRange(1, n)
            
