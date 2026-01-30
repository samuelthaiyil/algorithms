def invertTree(root):
    if not root:
        return

    left = invertTree(root.left)
    right = invertTree(root.right)

    root.right, root.left = left, right

    return root
    
