class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    # With value 
    def __init__(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        self.length = 1

    # Without value
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
        
# Create a Circular LinkedList with a value
cl = CSLinkedList(10)

# Print the head value
print(f"Head: {cl.head.value}")

# Print the tail value
print(f"Tail: {cl.tail.value}")

# Print the next value of the tail node which is the same as head
print(f"Tail's next value: {cl.tail.next.value}")

# Print the length
print(f"Length: {cl.length}")


# Create a Circular LinkedList without a value
# cl1 = CSLinkedList()
# print(cl1.head.value)       # Error no value
# print(cl1.head)             # Returns None