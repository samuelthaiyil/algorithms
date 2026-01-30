def sameTree(p, q) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)

    # INSERT_YOUR_CODE
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree 1
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)

# Tree 2 (same as t1)
t2 = Node(1)
t2.left = Node(2)
t2.right = Node(3)

# Tree 3 (different)
t3 = Node(1)
t3.left = Node(2)
t3.right = Node(4)

print(sameTree(t1, t2)) # True
print(sameTree(t1, t3)) # False

    
