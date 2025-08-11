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

    

    


l = CDLinkedList()
