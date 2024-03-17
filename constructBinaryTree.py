from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build a hashmap to store the index of value in inorder list
        self._index_map = {val: index for index, val in enumerate(inorder)}
        self._preorder = preorder
        self._inorder = inorder

        return self.helper(0, len(preorder) - 1, 0, len(inorder) - 1)


    def helper(self, pre_order_left: int, pre_order_right: int, in_order_left: int, in_order_right: int):
        # base case: there is only one element in both lists
        if pre_order_right - pre_order_left == 0:
            return TreeNode(self._preorder[pre_order_left])
        
        # if not, we construct the root node then recursively construct the left and right subtree
        root_val = self._preorder[pre_order_left]
        root = TreeNode(root_val)

        in_order_root_index = self._index_map[root_val]

        left_nodes_size = in_order_root_index - in_order_left
        right_nodes_size = in_order_right - in_order_root_index

        if left_nodes_size > 0:
            root.left = self.helper(pre_order_left + 1, pre_order_left + left_nodes_size, in_order_left, in_order_root_index - 1)
        
        if right_nodes_size > 0:
            root.right = self.helper(pre_order_right - right_nodes_size + 1, pre_order_right, in_order_root_index + 1, in_order_right)

        return root


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Preorder and inorder lists have one element
    preorder = [1]
    inorder = [1]
    result = solution.buildTree(preorder, inorder)
    assert result.val == 1
    assert result.left is None
    assert result.right is None

    # Test case 2: Preorder and inorder lists have multiple elements
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = solution.buildTree(preorder, inorder)
    assert result.val == 3
    assert result.left.val == 9
    assert result.right.val == 20
    assert result.right.left.val == 15
    assert result.right.right.val == 7

    print("All test cases pass")

    