def maxDepth(root):
    if not root:
        return False
    return max(maxDepth(root.left), maxDepth(root.right)) + 1