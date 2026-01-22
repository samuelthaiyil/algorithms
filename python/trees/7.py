def averageOfLevels(root):
    res = []
    q = [root]

    while q:
        level_size = len(q)
        sum = 0
        
        for _ in range(level_size):
            node = q.pop(0)
            sum += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(float(sum / level_size))
    
    return res