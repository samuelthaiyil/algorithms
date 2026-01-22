def isBST(root):
    def dfs(low, node, high):
        if not (low < node.val < high):
            return False
        
        return dfs(low, node.left, node.val) and dfs(node.val, node.right, high)
    
    return dfs(float("-inf"), root, float("inf"))