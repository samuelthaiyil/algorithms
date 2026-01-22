def invertBinaryTree(root):
    if not root:
        return None
    
    right = invertBinaryTree(root.right)
    left = invertBinaryTree(root.left)

    root.left = right
    root.right = left

    return root