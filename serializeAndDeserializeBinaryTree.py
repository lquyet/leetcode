from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Quite intuitive, we can use preorder traversal to serialize the tree, and note which nodes is leaf node by using 'null
# To reconstruct the tree, we can simply do the same process and build the tree from root.
# The time complexity is O(n) which n is the number of nodes in the tree, and the space complexity is also O(n) since we need to store the entire tree.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return 'null'
            return str(root.val) + ',' + preorder(root.left) + ',' + preorder(root.right)
        
        return preorder(root)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str 
        :rtype: TreeNode
        """
        
        nodes = data.split(',')

        def build(nodes: List[str]):
            val = nodes.pop(0)
            if val == 'null':
                return None
            root = TreeNode(int(val))
            root.left = build(nodes)
            root.right = build(nodes)
            return root
        
        return build(nodes)


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    cc = Codec()
    print(cc.serialize(root))
    # deser = Codec()
    ans = cc.deserialize(cc.serialize(root))

    print(ans.val)
    print(ans.left.val)
    print(ans.right.val)
    print(ans.right.left.val)
    print(ans.right.right.val)
   