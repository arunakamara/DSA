class Node:
    """
    Node is the fundamental block for a LinkedList
    """
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"<Node: [{self.value}]>"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        if self.length == 0:
            return f"[]"
        else:
            current = self.head
            node = []
            while current:
                if current == self.head:
                    node.append(f"[Head: {current.value}]")
                elif current == self.tail:
                    node.append(f"[Tail: {current.value}]")
                else:
                    node.append(f"[{current.value}]")
                current = current.next
            return " -> ".join(node)
        
    def append(self, value):
        """
        To add a new node at the end of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # Create a new node with the given value 
        new_node = Node(value)

        # If the list is empty, assign both head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # tail points to the new_node and assign tail the value of the new node
        else:              
            self.tail.next = new_node
            self.tail = new_node

        # Increment the length
        self.length += 1

    def prepend(self, value):
        """
        To add a new node at the beginning of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # Create a new node with the given value
        new_node = Node(value)

        # If list is empty, assign both head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Else the new node points to head and assign head the new node
        else:
            new_node.next = self.head
            self.head = new_node
        
        # Increment the length
        self.length += 1

    
    def insert(self, index, value):
        """
        To add a node at a specific position (zero-based index)
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Insert at the beginning
        if index == 0:
            return self.prepend(value)
        
        # Insert at the end
        elif index == self.length or index == -1:
            return self.append(value)
        
        # For invalid index we return False
        if index < 0 or index > self.length:
            return False
        
        # Create a new node
        new_node = Node(value)
        
        # Use a temp variable to loop through starting at head
        current = self.head

        # Loop from head to the node just before the node at the given index
        for _ in range(index-1):
            current = current.next
        
        # New node points to the node at the index position
        new_node.next = current.next

        # The node just before the given index now points to the new node
        current.next = new_node
        
        # Increment the length
        self.length += 1

        
    def traverse(self):
        """
        To print all the node values in the linked_list
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Use a pointer current and initialize it to the head
        current = self.head

        # Loop through the linked_list till the end
        while current:
            print(current.value)
            current = current.next
        
    def search(self, target):
        """
        Returns the index of the target value if present else returns -1
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Initialize current as a temp pointer to the head
        current = self.head

        # Initialize index as 0 for zero-based indexing
        index = 0

        # Loop through the list
        while current:

            # If current node value equal to target return its index
            if current.value == target:
                return index
            
            else:

                # current points to the next node and increment index by 1
                current = current.next
                index += 1

        # Return -1 if not found
        return -1
    
    def get(self, index):
        """
        Returns the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Return None for invalid index
        if index < -1 or index >= self.length:
            return None
        
        # Return the last node for index -1
        if index == -1:
            return self.tail

        # Initial the pointer to head
        current = self.head

        # Increment pointer till it points to the given index
        for _ in range(index):
            current = current.next
        
        # Return the node at the given index
        return current
    
    def set_value(self, index, value):
        """
        Updates the value of a node at the given index and returns True else returns False
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Use the get method to get the node at the given index
        node = self.get(index)

        # If such node exits, update its value and return True else return False
        if node:
            node.value = value
            return True
        return False
            

    def pop_first(self):
        """
        Delete and returns the first node from the list else returns None
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        # Return None if the list is empty
        if self.head is None:
            return None
        
        # Assign the node that is going to be deleted to popped_node
        popped_node = self.head
        
        # Assign both head and tail to None if the length is 1
        if self.length == 1:
            self.head = None
            self.tail = None

        else:

            # Make head points to the next node
            self.head = self.head.next

            # Make the deleted node point to None to disconnect it from the rest of the list
            popped_node.next = None
        
        # Decrement the length by 1
        self.length -= 1

        # Return the deleted node
        return popped_node
    

    def pop(self):
        """
        Deletes and returns the last node from the list else returns None
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # If the list is empty return None
        if self.head is None:
            return None
        
        # Assign popped_node the last node
        popped_node = self.tail

        # Assign both head and tail to None if length is 1
        if self.length == 1:
            self.head = None
            self.tail = None

        else:

            # Use a temporary pointer to locate the second-to-last node
            current = self.head

            # Move the pointer to the its next node till it reaches the node just before the tail
            while current.next is not self.tail:
                current = current.next

            # Make tail points to the second-to-last node making it the new tail
            self.tail = current

            # Make the second-to-last node next be None to disconnect it from the previous tail
            current.next = None
        
        # Decrement the value of length
        self.length -= 1

        # Return the deleted node
        return popped_node


    def remove(self, index):
        """
        Delete and return the node at the given index else returns None
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Return None if the index is greater than the length of the list or less than -1
        if index >= self.length or index < -1:  
            return None
        
        # If the index is 0, return the pop_first method
        if index == 0:
            return self.pop_first()
        
        # Return pop method if index is -1 or equal to the length - 1
        if index == self.length - 1 or index == -1:
            return self.pop()
        
        # Use the get method to the node just before the node at the given index
        prev_node = self.get(index-1)

        # Assign the node at the given index to popped_node
        popped_node = prev_node.next

        # Make the node before the popped_node points to the node after the popped_node
        prev_node.next = popped_node.next

        # To disconnect the popped_node from the rest of the list, assign its next node to None
        popped_node.next = None

        # Decrement the value of length
        self.length -= 1

        # Return the popped_node
        return popped_node
        

