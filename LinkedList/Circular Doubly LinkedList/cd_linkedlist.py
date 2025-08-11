class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.prev} <-> {self.value} <-> {self.next}"
    
class CDLinkedList:
    # def __init__(self):
    #     """With no element"""
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

    def __init__(self, value):
        """With one element"""
        node = Node(value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        self.length = 1
