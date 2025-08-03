from linkedlist_class import LinkedList

def remove_duplicates(l_list):
        """
        Takes a linkedlist as input and return it with only its unique values
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Returns None if list is empty
        if not l_list.head:
            return
        
        # Initialize an empty set to keep track of unique values
        node_values = set()

        # Initialize current node as the head
        cur_node = l_list.head
        
        # Adds the first value
        node_values.add(cur_node.value)
        
        # Loop through to the last node
        while cur_node.next:

            # Skip the next node and decrement the length if its value is already in the set
            if cur_node.next.value in node_values:
                cur_node.next = cur_node.next.next
                l_list.length -= 1 

            else:

                # Add the next node if its value is not in the set
                node_values.add(cur_node.next.value)

                # Move current node to the next node
                cur_node = cur_node.next
        # Update the tail value to the current node which is the new last node
        l_list.tail = cur_node


