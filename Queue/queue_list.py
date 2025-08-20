class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [ str(x) for x in self.items ]
        return ' '.join(values)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items.append(value)
        return f"The element {value} is inserted at the end of the queue."
    

my_queue = Queue()
print(my_queue)