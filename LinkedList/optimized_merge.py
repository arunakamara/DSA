from linkedlist_class import LinkedList, Node
def merge_sorted_lists(list1, list2):
    """
    Merges two sorted LinkedList objects into a new sorted LinkedList
    without modifying the originals. Efficiently tracks tail and length.
    """

    dummy = Node(0)
    current = dummy
    ptr1 = list1.head
    ptr2 = list2.head

    merged_list = LinkedList()  # Dummy init, will overwrite head later
    # merged_list.length = 0

    # Actual merge
    while ptr1 and ptr2:
        if ptr1.value <= ptr2.value:
            current.next = ptr1
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2 = ptr2.next
        current = current.next
        merged_list.length += 1
        merged_list.tail = current

    # Attach remaining nodes
    remaining = ptr1 if ptr1 else ptr2
    while remaining:
        current.next = remaining
        current = current.next
        merged_list.length += 1
        merged_list.tail = current
        remaining = remaining.next

    # Finalize head (skip dummy)
    merged_list.head = dummy.next

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

merged = merge_sorted_lists(l1,l2)
print(merged)
print(merged.length)