from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


    def __repr__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next
    
    def __repr__(self):
        values = [ str(x.value) for x in self ]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0

        current = self.head

        while current:
            result += 1
            current = current.next
        
        return result
    

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:

            self.tail.next = new_node
            self.tail = new_node

        return self.tail
    

    def generate(self, n, min_value, max_value):
        """
        Returns a linkedlist with random values
        """

        for _ in range(n):
            self.add(randint(min_value, max_value))


def main():
    l = LinkedList()
    print(l)
    l.generate(10, 5, 15)
    print(l)
    print(len(l))
    

if __name__ == "__main__":
    main()
        
