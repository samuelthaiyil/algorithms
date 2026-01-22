def isSubtree(root, subroot):
    def dfs(root, res):
        if not root:
            res.append("#")
            return
        
        # preorder traversal
        res.append(f"_{root.val}_")
        dfs(root.left)
        dfs(root.right)
    
    tree, subtree = [][]

    dfs(root, tree)
    dfs(subroot, subtree)

    return "".join(subtree) in "".join(tree)

    
