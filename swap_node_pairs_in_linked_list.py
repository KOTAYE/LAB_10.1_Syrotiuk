from preloaded import Node

def swap_pairs(head):
    initial = Node(0)
    initial.next = head
    current = initial

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        first.next = second.next
        second.next = first
        current.next = second
        
        current = first

    return initial.next