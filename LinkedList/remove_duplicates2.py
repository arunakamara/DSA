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


head = NodeList(1)
n1 = NodeList(2)
n2 = NodeList(2)
n3 = NodeList(3)
n4 = NodeList(4)
n5 = NodeList(4)
n6 = NodeList(5)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

remove_duplicates(head)
