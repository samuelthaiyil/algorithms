def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root)
    inorder(root.right)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

# Create a sample tree:
#      1
#     / \
#    2   3
#   /
#  4
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3)


inorder(root)
