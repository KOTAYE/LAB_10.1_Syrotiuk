class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s == "None":
        return None
    values = s.split(" -> ")[:-1]
    head = None
    
    for value in reversed(values):
        head = Node(int(value), head)
    
    return head