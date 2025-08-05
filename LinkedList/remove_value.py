from linkedlist_class import LinkedList, Node


def remove_val(l_list, val):
    if not l_list.head:
        return None
    
    dummy = Node(-1)
    dummy.next = l_list.head
    current = l_list.head
    prev_node = dummy

    while current:
        if current.value == val:
            prev_node.next = current.next
            current = current.next
        else:
            prev_node = current
            current = current.next
    
    return l_list




l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(14)
l.append(4)
l.append(5)
l.append(14)

print(l)

print(remove_val(l, 14))

