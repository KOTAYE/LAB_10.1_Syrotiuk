def loop_size(node):
    if not node or not node.next:
        return 0
    
    slow = node
    fast = node
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return 0
    
    loop_length = 1
    current = slow.next
    
    while current != slow:
        loop_length += 1
        current = current.next
    
    return loop_length