from linkedlist_class import LinkedList, Node


def remove_val(l_list, val):
    """
    Removes the given value from the linked list and returns the list
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    if not l_list.head:
        return None
    
    # Initialize a dummy node to use as a prev_node
    dummy = Node(-1)

    # Connect the dummy node to the list
    dummy.next = l_list.head

    # Use the pointer current and assign it to the head of the list
    current = l_list.head

    # Assign prev_node to the node before the head of the list
    prev_node = dummy

    while current:
        # If the current value equals the given value skip the current value
        if current.value == val:
            # The node before the current node directly points to the node after the current value
            prev_node.next = current.next   
            # The current node points to the node before it, the same as prev_node.next
            current = current.next
        else:
            # Move both prev_node and current pointers forward
            prev_node = current
            current = current.next
    # return the list
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

