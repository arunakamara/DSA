from linkedlist_quest import LinkedList

def partition(ll, x):
    """
    Arrange the list such that all nodes with value less than x are on the left
    and all nodes with value greater than x are on the right
    Time Complexity - O(n)
    Space Complexity - O(1)
    """

    # Point current and tali to the head
    current = ll.head
    ll.tail = ll.head
    

    # Loop through the list
    while current:


        # Store the current node's next node 
        # and detach the current node from the list
        next_node = current.next
        current.next = None

        # Add current node at the beginning if less than x
        if current.value < x:
            current.next = ll.head
            ll.head = current
        
        # Add current node at the end if greater than x
        else:
            
            ll.tail.next = current
            ll.tail = current

        # Move to the next node
        current = next_node

      
    # If all nodes are less than x,
    # Set tail.next to None instead of it pointing to itself
    if not ll.tail.next:
        ll.tail.next = None




l = LinkedList()
l.generate(10, 1, 20)
print(l)
partitioned_list = partition(l, 15)
print(l)