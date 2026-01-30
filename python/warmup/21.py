def reverseList(head):
    curr = head
    prev = None

    while curr:
        # store true next node
        next = curr.next

        # switch arrow
        curr.next = prev

        # advance pointers
        prev = curr 
        curr = next
    
    return prev

