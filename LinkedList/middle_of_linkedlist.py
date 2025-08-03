from linkedlist_class import LinkedList

def find_middle(l_list):
    """
    Find and return the middle node of a singly linked list. 
    If the list has an even number of nodes, return the second of the two middle nodes.
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    
    # Return None for an empty list
    if not l_list.head:
        return None
    
    # Initialize both pointers to the head
    fast = slow = l_list.head

    # Loops from the the start, head to the second to last or last of the list
    while fast and fast.next:

        # Moves one node forward
        slow = slow.next

        # Moves two nodes forward
        fast = fast.next.next

    # Returns slow which is half of the length of the list
    return slow

