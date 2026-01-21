class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    sentinel = ListNode(0, head)
    pred = sentinel

    while head:
        # duplicate is found
        if head.next and head.next.val == head.val:
            # skip passed all the duplicates by setting head to head.next
            while head.next and head.val == head.next.val:
                head = head.next
            # once we land a non-duplicate set the pred's next value to point to it 
            pred.next = head.next
        else:
            pred = pred.next
        
        head = head.next
    
    return sentinel.next
            
def printList(head):
    while head:
        print(head.val)
        head = head.next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
printList(node1)
removeDuplicates(node1)
print("After removing duplicates:")
printList(node1)







