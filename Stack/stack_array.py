class Stack:
    def __init__(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        self.items = []

my_stack = Stack()

# Because we're using list no need to
# track the length we can simply len() method
print(len(my_stack.items))