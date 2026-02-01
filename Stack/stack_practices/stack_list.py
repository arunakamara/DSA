class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        if self.is_empty():
            return "Stack is empty."
        
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)
    
    def __str__(self):
        return self.__repr__()
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.is_empty():
            return "Stack is already empty"
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

s = Stack()
s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50)
print(s)