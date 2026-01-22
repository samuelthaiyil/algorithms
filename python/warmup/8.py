def treeTraversal(root):
    if not root:
        return []
        
    q = [root]
    res = []

    while q:
        level = []
        level_size = len(q)

        for _ in range(level_size):
            node = q.pop(0)
            level.append(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(level)
    
    return res