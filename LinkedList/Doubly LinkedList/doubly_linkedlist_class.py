class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

    def __repr__(self):
        return str(self.value)
        # return f"{self.prev} <- [{self.value}] -> {self.next}"


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
            

    def append(self, value):
        """
        Adds a new node to the end of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        # Create a new node
        new_node = Node(value)

        # If the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
    



