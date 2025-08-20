class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [ str(x) for x in self.items ]
        return ' '.join(values)
    
    def is_empty(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        return len(self.items) == 0
    
    def enqueue(self, value):
        """
        Time Complexity - O(1) / O(n)
        Space Complexity - O(1)
        """
        self.items.append(value)
        return f"The element {value} is inserted at the end of the queue."
    

my_queue = Queue()
print(my_queue)