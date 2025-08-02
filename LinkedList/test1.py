class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<Node: {self.value}>"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        if self.head is None:
            return "[]"
        
        current = self.head
        node = []

        while current:
            if current == self.head:
                node.append(f"[Head: {current.value}]")
            elif current == self.tail:
                node.append(f"[Tail: {current.value}]")
            else:
                node.append(f"[{current.value}]")
            
            current = current.next
            
        return " -> ".join(node)
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node
        self.length += 1

    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        
        if index == self.length or index == -1:
            return self.append(value)
    
        if index < -1 or index > self.length:
            return None
        
        node = Node(value)

        current = self.head
        for _ in range(index-1):
            current = current.next

        node.next = current.next
        current.next = node

        self.length += 1


    def traverse(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head

        index = 0

        while current:
            if current.value == target:
                return index
            else:
                current = current.next
                index += 1
        return None
    

    def get(self, index):
        if index < -1 or index >= self.length:
            return None
        
        if index == -1:
            return self.tail

        current = self.head

        for _ in range(index):
            current = current.next
        
        return current

    def set(self, index, value):

        node = self.get(index)

        if node:
            node.value = value
            return True
        return False
    

    def pop_first(self):

        if self.head is None:
            return None
        
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node.next = None

        self.length -= 1

        return popped_node
            

    def pop(self):
        if self.head is None:
            return None
        
        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = self.get(self.length-1)
            self.tail = prev_node
            prev_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, value):
        if self.head is None:
            return None
        node_index = self.search(value)

        print(node_index)

        if node_index:
            prev_node = self.head
            node = self.get(node_index)

            for _ in range(node_index-1):
                prev_node = prev_node.next

            prev_node.next = node.next
            node.next = None

            self.length -= 1

            return node
        
        return None
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)


        
            
