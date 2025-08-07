class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    # def __init__(self, value):
    #     """ With value """
    #     node = Node(value)
    #     node.next = node
    #     self.head = node
    #     self.tail = node
    #     self.length = 1

    
    def __init__(self):
        """Without value"""
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, value):
        """
        Adds a new node to the end of the list
        Time Complexity - O(1)
        SPace Complexity - O(1)
        """

        new_node = Node(value)

        # Check if the node is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node

        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1 


csl = CSLinkedList()
csl.append(10)
csl.append(20)
print(csl.head.value)
print(csl.head.next.value)
print(csl.tail.next.value == csl.head.value)
        
