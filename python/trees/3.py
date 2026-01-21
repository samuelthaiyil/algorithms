def isSymmetric(root):
    def isMirror(node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
        
        return isMirror(node1.left, node2.right) and isMirror(node2.left, node1.right)
    
    return isMirror(root, root)

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Example symmetric tree:
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))  # Should print True

# Example asymmetric tree:
#       1
#      / \
#     2   2
#      \   \
#      3    3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print(isSymmetric(root2))  # Should print False
