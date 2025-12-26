# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs_count(root, None)
        return self.count
    
    def dfs_count(self, root: TreeNode, max_parent):
        if not root:
            return
        
        if max_parent is None or max_parent <= root.val:
            print("checking node: ", root.val, " max_parent: ", max_parent)
            self.count += 1

        current_max = None
        if max_parent != None:
            current_max = root.val if root.val > max_parent else max_parent
        else:
            current_max = root.val

        self.dfs_count(root.left, current_max)
        self.dfs_count(root.right, current_max)


if __name__ == "__main__":
    solution = Solution()
    # Create a binary tree for testing [3,1,4,3,null,1,5]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    # Call the goodNodes function and print the result
    result = solution.goodNodes(root)
    print(result)




    