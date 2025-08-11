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
        
        # current = None

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



l = CDLinkedList()
l.append(5)
l.append(6)
l.append(7)
l.prepend(4)
l.prepend(3)

l.get(2)