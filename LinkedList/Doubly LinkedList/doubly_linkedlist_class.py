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

    def search(self, target):
        """
        Returns the index of the target else -1
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if not self.head:
            return None
        
        current = self.head
        index = 0

        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1

        return -1

    def get(self, index):
        """
        Returns the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        # Returns None for invalid index
        if index < 0 or index >= self.length:
            return None

        # Find the middle of the list
        # and traverse from the the head if the index is in the first part
        if index <= self.length // 2:
            current = self.head

            for _ in range(index):
                current = current.next

        else:

            # Traverse from the tail of the second part
            current = self.tail

            for _ in range(self.length-1, index, -1):
                current = current.prev
        
        # Return the node at the given index
        return current

    def set_value(self, index, value):
        """
        Update the value of the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        node = self.get(index)

        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Inserts a new node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        if index < 0 or index > self.length:
            print("Index out of bound.")
            return
        
        new_node = Node(value)

        if index == 0:
            self.prepend(value)
            return
        
        elif index == self.length:
            self.append(value)
            return
        
        # Get the node just before the node at the given index
        current = self.get(index-1)

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.length += 1

    def pop_first(self):
        """
        Delete and return the first node
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if not self.head:
            return None
        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None

        else:

            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None

        self.length -= 1
        return popped_node

    def pop(self):
        """
        Delete and return the last node from the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        if not self.head:
            return None
        
        popped_node = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None
        
        self.length -= 1
        return popped_node

    def remove(self, index):
        """
        Deletes and return the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            popped_node = self.get(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.length -= 1
            return popped_node




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