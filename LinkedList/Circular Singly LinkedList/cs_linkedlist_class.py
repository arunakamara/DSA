class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<Node: {self.value}>"


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

    def __repr__(self):
        # Initialize the current to the head node and result to an empty string
        current = self.head
        result = ''

        # Loop till the end of the list
        while current:
            result += str(current.value)
            current = current.next

            # Check if the current node is equal to the head node
            # If it is break
            if current is self.head:
                break
            result += ' -> '
        
        return result


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

    def prepend(self, value):
        """
        Adds a new node at the beginning of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        
        self.length += 1
        
    def insert(self, index, value):
        """
        Adds a new node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if index < 0 or index > self.length:
            raise Exception("Index out of range")
        
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            current = self.head

            for _ in range(index-1):
                current = current.next

            new_node.next = current.next
            current.next = new_node
            
            self.length += 1

    def traverse(self):
        """
        Prints out the values of each node in the list
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        current = self.head

        while current:
            print(current.value)
            current = current.next
            
            # Exit the loop if we are back at the head node
            if current == self.head:
                break

    def search(self, target):
        """
        Returns the index of the target value else -1 
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        
        current = self.head
        index = 0

        while current:
            if current.value == target:
                return index
            else:
                # Exit the loop if the next node of the current node is equal to head
                # if current.next == self.head:
                if current is self.tail:
                    break
                current = current.next
                index += 1
        return -1
    

    def get(self, index):
        """
        Returns the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        
        current = self.head

        for _ in range(index):
            current = current.next

        return current
    
    def set_value(self, index, value):
        """
        Update the value of the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """
        node = self.get(index)

        if node:
            node.value = value
            return True
        else:
            return False

                


csl = CSLinkedList()
csl.append(10)
csl.append(20)
csl.append(30)
csl.append(40)
csl.append(50)
print(csl)

        
