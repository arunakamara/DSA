class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next
    
    def __repr__(self):
        values = [ str(x.value) for x in self ]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0

        current = self.head

        while current:
            result += 1
            current = current.next
        
        return result
    

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:

            self.tail.next = new_node
            self.tail = new_node

        return self.tail
    
    
        
    