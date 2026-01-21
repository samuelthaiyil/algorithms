def dfs(root):
    if not root:
        return
    
    print(root.val)
    dfs(root.left) 
    dfs(root.right)

def bfs(root):
    if not root:
        return
    
    q = [root]

    while q:
        node = q.pop(0)
        print(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# Building a binary tree with another layer:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

bfs(root)

