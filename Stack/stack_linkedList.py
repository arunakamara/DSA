class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # def __init__(self, value):
    #     """With a value"""
    #     new_node = Node(value)
    #     self.top = new_node
    #     self.length = 1


    def __init__(self):
        """Without a value"""
        self.top = None
        self.length = 0

    
    def push(self, value):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
    