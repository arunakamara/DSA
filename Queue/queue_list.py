class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        values = [ str(x) for x in reversed(self.items) ]
        return f"front {' '.join(values)} rear" 
    
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
        # self.items.append(value) - Time Complexity: Amortized 

        self.items.insert(0, value) # Time Complexity: O(n)

        return f"The element {value} is inserted at the end of the queue."
    
    def dequeue(self):
        if self.is_empty():
            return "The queue is empty."
        
        # return self.items.pop(0)  - Time Complexity: O(n)

        return self.items.pop() # Time Complexity: O(1)
    
    def peek(self):
        if self.is_empty():
            return "The queue is empty"

        return self.items[0]
    
    def delete(self):
        self.items = None

    

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue)

print(my_queue)
# print(my_queue.enqueue(5))
# print(my_queue)
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue)

print(my_queue.peek())