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
    merged_list.length = 0

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

