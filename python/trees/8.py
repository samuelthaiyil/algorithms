def sameTree(t1, t2) -> bool:
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.val != t2.val:
        return False
    
    return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

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

    
