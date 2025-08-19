class Stack:
    def __init__(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        if self.is_empty():
            return "Stack is empty"
        
        # Using list comprehension to create a new list of strings 
        # from a reversed iterator of self.items
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)


    def push(self, element):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        self.items.append(element)

    def pop(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()


# Because we're using list no need to
# track the length we can simply len() method
# print(len(my_stack.items))

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack)
print(f"POPPED: {my_stack.pop()}")
print(f"POPPED: {my_stack.pop()}")
print(f"POPPED: {my_stack.pop()}")
print(f"POPPED: {my_stack.pop()}")
print(my_stack)
 
