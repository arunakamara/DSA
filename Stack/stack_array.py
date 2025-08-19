class Stack:
    def __init__(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        self.items = []

    def push(self, element):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        self.items.append(element)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack.items)


# Because we're using list no need to
# track the length we can simply len() method
print(len(my_stack.items))