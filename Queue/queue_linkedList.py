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
        """
        Time Complexity - O(1) 
        Space Complexity - O(1)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return f"{value} has been added to the end of the queue"
    
    def is_empty(self):
        return self.head is None
    

    def dequeue(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if self.is_empty():
            return "Queue is already empty."
        
        else:
            front = self.head

            if self.length == 1:
                self.head = self.tail = None
            
            else:
                self.head = self.head.next
                front.next = None
            
            self.length -= 1
            print(front.next)
            return front
                
        
       
    

    


q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q)

print(q.dequeue())