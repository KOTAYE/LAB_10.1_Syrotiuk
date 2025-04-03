class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    
    odd_head = Node()
    even_head = Node()
    
    odd = odd_head
    even = even_head
    
    current = head
    is_odd = True
    
    while current:
        if is_odd:
            odd.next = current
            odd = odd.next
        else:
            even.next = current
            even = even.next
        
        current = current.next
        is_odd = not is_odd
    
    odd.next = None
    even.next = None
    
    return Context(odd_head.next, even_head.next)