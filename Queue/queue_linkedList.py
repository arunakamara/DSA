class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    # 