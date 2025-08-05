class NodeList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}  "

def remove_duplicates(head):
    if not head:
        return None
    
    seen = set()
    dummy = NodeList(-1)

    dummy.next = head
    prev_node = dummy
    current = head

    while current:
        if current.value in seen:
            prev_node.next = current.next
            print(prev_node.next)
            current = current.next
        else:
            seen.add(current.value)
            current = current.next
    return dummy.next


remove_duplicates(head)
