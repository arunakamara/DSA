class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"
    

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        values = [ str(x) for x in self]
        return ' '.join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return f"{value} has been added to the end of the queue"
    

    


q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q)
