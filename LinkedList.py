class Node:
    """
    Node is the fundamental block for a LinkedList
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"<Node: [{self.data}]>"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        if self.length == 0:
            return f"[]"
        else:
            current = self.head
            node = []
            while current:
                if current == self.head:
                    node.append(f"[Head: {current.data}]")
                elif current == self.tail:
                    node.append(f"[Tail: {current.data}]")
                else:
                    node.append(f"[{current.data}]")
                current = current.next
            return " -> ".join(node)
        
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
            


l = LinkedList()
