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

    def __repr__(self):
        if self.head is None:
            return "empty List"
        
        current = self.head
        result = ""

        while current:
            result += str(current.value)
            
            if current.next:
                result += ' <-> '
            
            current = current.next
    
        return result

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
    
    def prepend(self, value):
        """
        Adds a new node at the beginning of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def traverse(self):
        """
        Prints out each value in the list starting from the head
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        current = self.head 

        while current:
            print(current.value)
            current = current.next
        
    def reverse_traverse(self):
        """
        Prints each value of the list in the reverse order
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        current = self.tail

        while current:
            print(current.value)
            current = current.prev




l = DoubleLinkedList()
print(l)
l.append(10)
print(l)
l.append(20)
print(l)
l.append(30)
print(l)
l.append(40)
print(l)