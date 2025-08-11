class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)
    
class CDLinkedList:
    def __init__(self):
        """With no element"""
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self, value):
        # """With one element"""
        # node = Node(value)
        # node.next = node
        # node.prev = node
        # self.head = node
        # self.tail = node
        # self.length = 1

    def __repr__(self):

        if not self.head:
            return "Empty List"
        
        current = self.head
        result = ''

        while current:
            result += str(current.value)
            current = current.next

            if current is self.head:
                break

            result += ' <-> '
        
        return result

    def append(self, value):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node

        else:

            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node

        else:

            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        
        self.length += 1

    def traverse(self):
        """
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        current = self.head

        while current:

            print(current.value)
            current = current.next
            if current is self.head:
                break

    def reverse_traverse(self):
        """
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        current = self.tail

        while current:

            print(current.value)
            current = current.prev
            
            if current is self.tail:
                break

    def search(self, value):
        """
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        current = self.head
        index = 0
        
        while current:
            if current.value == value:
                return index
            
            current = current.next
            index += 1

            if current is self.head:
                break

        return -1

    def get(self, index):
        """
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if index < 0 or index >= self.length:
            return None
        

        if index < self.length // 2:
            current = self.head

            for _ in range(index):
                current = current.next
            
            return current
        
        else:

            current = self.tail

            for _ in range(self.length-1, index, -1):
                current = current.prev

            return current

    def set_value(self, index, value):
        """
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
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return 
        
        if index == 0:
            return self.prepend(value)
        
        elif index == self.length:
            return self.append(value)
        
        else:

            new_node = Node(value)

            current = self.head

            for _ in range(index-1):
                current = current.next

            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.length += 1

    def pop_first(self):
        """
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

            self.head = popped_node.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head            

        self.length -= 1

        return popped_node

    def pop(self):
        """
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
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -= 1

        return popped_node








l = CDLinkedList()
l.append(5)
l.append(6)
l.append(7)
l.prepend(4)
l.prepend(3)

l.get(2)