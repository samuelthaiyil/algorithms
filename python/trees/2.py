class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def countLeaves(root) -> int:
    # base cases
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    
    # recursive step
    return countLeaves(root.left) + countLeaves(root.right)

# Example tree:
#       4
#      / \
#     2   6
#    /   / \
#   1   5   7
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(countLeaves(root))  # Should print 3 (leaves: 1, 5, 7)
