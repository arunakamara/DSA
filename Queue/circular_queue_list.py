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
        
