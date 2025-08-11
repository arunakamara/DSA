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

    


l = CDLinkedList()
