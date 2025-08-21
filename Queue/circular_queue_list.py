class CQueue:
    def __init__(self, max_size):
        """
        Time Complexity - O(1)
        Space Complexity - O(n)
        """
        self.items = max_size * [None]
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def __repr__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    

    def is_full(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        # Check when the rear pointer is now in front of the front
        # Checks if there is no empty space between the rear and the front
        if self.rear + 1 == self.front:
            return True
        
        # Checks if the front is at the beginning and the rear is at the end
        elif self.front == 0 and self.rear + 1 == self.max_size:
            return True
        
        else:
            return False
        
    def is_empty(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if self.front == -1 and self.rear == -1:
            return True 
        else:
            return False
        

    def enqueue(self, value):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        # If queue is already full
        if self.is_full():
            return f"Queue is already full"
        
        # If the last element added is already at the end but queue is not yet full
        # We set rear to the beginning of the queue
        if self.rear + 1 == self.max_size:
            self.rear = 0
        
        # If there is more space that is rear is yet to reach the end of the queue
        else:
            self.rear += 1

            # If the queue is empty then set front to 0 (because it was initial -1)
            if self.front == -1:
                self.front = 0
        
        # Add the new element at the rear position
        self.items[self.rear] = value

        return f"The element {value} is add at the end of the queue."
    

    def dequeue(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        if self.is_empty():
            return "The queue is already empty."
        
        else:
            # Get the element at the front
            first_element = self.items[self.front]

            # Get the index of the front element for future reference 
            front = self.front

            # Check if there is only one element in the queue
            if self.front == self.rear:
                self.front = -1
                self.rear = -1

            # Check if the front is at the end of the queue
            elif self.front + 1 == self.max_size:
                self.front = 0

            else:
                self.front += 1

            # Set the value at the index of front to None
            self.items[front] = None

            return first_element

    def peek(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if self.is_empty():
            return "The queue is empty."
        
        else:
            return self.items[self.front]
            
    def delete(self):
        self.items = self.max_size * [None]
        self.rear = -1
        self.front = -1


q = CQueue(5)

print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)

q.peek()
