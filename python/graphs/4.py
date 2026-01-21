class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(4)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(sameTree(p, q))