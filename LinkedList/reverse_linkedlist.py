from linkedlist_class import LinkedList

def reverse(l_list):
    """
    Input: linkedlist
    Output: reverses the input in place
    Time Complexity - O(n)
    Space Complexity - O(1)
    """
    # Return the list as it is if it's empty or contains a single element
    if l_list.length == 0 or l_list.length == 1:
        return l_list

    # Initialize prev_node as None 
    prev_node = None

    # Initialize cur_node as head
    cur_node = l_list.head

    # Loop through the list to the end
    while cur_node is not None:

        # Keep track of the next node before reassigning it to prev
        next_node = cur_node.next

        # Points current backwards
        cur_node.next = prev_node

        # Increment prev to the next node
        prev_node = cur_node

        # Increment current to the next node
        cur_node = next_node

    # Swap the head and tail of the list
    l_list.head, l_list.tail = l_list.tail, l_list.head

    return l_list
