

def nthToLast(ll, n):
    """
    Returns the nth element from the last
    """

    # Initialize both pointer to head
    pointer1 = ll.head
    pointer2 = ll.head

    # Put both pointers n-node apart
    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    # Move both pointer one step ahead until the second pointer reaches the tail
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    # Return pointer
    return pointer1



