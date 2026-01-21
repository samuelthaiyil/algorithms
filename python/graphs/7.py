class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(p, i):
    visited = set()

    def preorder(root, visited):
        if not root:
            return
            
        visited.add(root.val)
        preorder(root.left, visited)
        preorder(root.right, visited)
    
    preorder(p, visited)
    
    return visited

p = TreeNode(5)
p.left = TreeNode(6)
p.right = TreeNode(7)

q = TreeNode(2)
q.left = TreeNode(3)
q.right = TreeNode(4)

print(buildTree(p, q))