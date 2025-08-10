from linkedlist_class import LinkedList, Node


def merge(l1, l2):

    # Initialize a dummy node to build the new list from
    dummy = Node(0)

    # Initialize a pointer current to the dummy node used for adding nodes to the new list
    current = dummy

    # Pointers to the head of each node
    # We can't use the list themselves here because they don't have a value attribute 
    # but their heads which are just nodes have
    ptr1 = l1.head
    ptr2 = l2.head

    # Loop through and compare the nodes of both list until we reach the end of one 
    # Merge both lists until one is exhausted
    while ptr1 and ptr2:
        if ptr1.value <= ptr2.value:
            current.next = ptr1
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2 = ptr2.next
        current = current.next

    # Attach the remaining part of the non-exhausted list
    if ptr1:
        current.next = ptr1
    elif ptr2:
        current.next = ptr2

    # Build the new LinkedList from dummy.next
    merged_list = LinkedList()     
    merged_list.head = dummy.next


    # Fix tail and length 
    current = merged_list.head
    count = 1

    while current.next:
        current = current.next
        count += 1
    merged_list.tail = current


    merged_list.length = count

    return merged_list


l1 = LinkedList()
l2 = LinkedList()

l1.append(1)
l1.append(3)
l1.append(4)
l1.append(7)
l1.append(9)

l2.append(2)
l2.append(5)
l2.append(6)

print(l1)
print(l2)

merged = merge(l1,l2)
print(merged)
print(merged.length)