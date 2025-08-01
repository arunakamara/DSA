class Node:
    """
    Node is the fundamental block for a LinkedList
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"<Node: [{self.data}]>"

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
                    node.append(f"[Head: {current.data}]")
                elif current == self.tail:
                    node.append(f"[Tail: {current.data}]")
                else:
                    node.append(f"[{current.data}]")
                current = current.next
            return " -> ".join(node)
        
    def append(self, data):
        """
        To add a new node at the end of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # Create a new node with the given data 
        new_node = Node(data)

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

    def prepend(self, data):
        """
        To add a new node at the beginning of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # Create a new node with the given data
        new_node = Node(data)

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

    
    def insert(self, index, data):
        """
        To add a node at a specific position (zero-based index)
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Insert at the beginning
        if index == 0:
            return self.prepend(data)
        
        # Insert at the end
        elif index == self.length or index == -1:
            return self.append(data)
        
        # For invalid index we return False
        if index < 0 or index > self.length:
            return False
        
        # Create a new node
        new_node = Node(data)
        
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
        To print all the node values in the linkedlist
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # Use a pointer current and initialize it to the head
        current = self.head

        # Loop through the linked_list till the end
        while current:
            print(current.data)
            current = current.next
        
    def search(self, target):
        """
        Returns the index of the target value if present else -1
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
            if current.data == target:
                return index
            
            else:

                # current points to the next node and increment index by 1
                current = current.next
                index += 1

        # Return -1 if not found
        return -1
            
