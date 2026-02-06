def invertTree(root):
    if not root:
        return
    
    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left, root.right = right, left

    return root

