from linkedlist_quest import LinkedList 


def nthToLast(ll, n):
    """
    Returns the nth element from the last
    Time Complexity - O(n)
    Space Complexity - O(1)
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

l = LinkedList()
l.generate(10, 1, 20)
print(l)
print(nthToLast(l, 2))