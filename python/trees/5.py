def maxHeight(root) -> int:
    if not root:
        return 0
        
    return max(maxHeight(root.left), maxHeight(root.right)) + 1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2, Node(4))
root.right = Node(3)

print(maxHeight(root))   
