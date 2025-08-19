class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"

class Stack:
    # def __init__(self, value):
    #     """With a value"""
    #     new_node = Node(value)
    #     self.top = new_node
    #     self.length = 1


    def __init__(self):
        """Without a value"""
        self.top = None
        self.length = 0

    
    def __repr__(self):
        if self.is_empty():
            return "Stack is empty"
        
        result = ""
        current = self.top
        while current:
            if current.next:
                result += str(current.value) + "\n"
            else:
                result += str(current.value)
            
            current = current.next

        return result
            

    def is_empty(self):
        return self.length == 0

    
    def push(self, value):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        """
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        if self.top is None:
            return None
        
        popped_node = self.top
        if self.length == 0:
            self.top = None
        
        else:
            self.top = self.top.next
            popped_node.next = None
        
        self.length -= 1
        return popped_node

        

    

my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)

print(my_stack)

print()

print(f"Top: {my_stack.top}")

print(f"POPPED: {my_stack.pop()}")