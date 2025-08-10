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

    



