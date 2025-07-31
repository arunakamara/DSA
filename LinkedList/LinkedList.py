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
            


l = LinkedList()
