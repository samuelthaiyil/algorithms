class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def isBST(root):
    # dfs on node
    def dfs(low, node, high):
        # if node is none, reached end of tree successfully
        if not node:
            return True
        # if node's value isn't strictly between low and high return false, as it violates BST invariant
        elif not (low < node.val < high):
            return False
        # Run dfs recursively on both sides of the tree, left node and right node
        return dfs(low, node.left, node.val) and dfs(node.val, node.right, high)
    
    return dfs(float("-inf"), root, float("inf"))

# Example tree:
#       10
#      /  \
#     5   15
#        /  \
#       12  20
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

print(isBST(root))  # Should print True

# Not a BST: 17 is on the left of 15, violating BST property
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.right.left = TreeNode(17)
root2.right.right = TreeNode(20)

print(isBST(root2))  # Should print False


