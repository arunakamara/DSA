from cs_linkedlist_class import CSLinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<Node: {self.value}>"
        
class csLinkedList(CSLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __repr__(self):
        if self.head is None:
            return '[]'
        
        current = self.head
        result = ''

        while current:
            result += str(current.value)
            current = current.next
            if current is self.head:
                break
            result += ' -> '

    def count(self):
        if self.head is None:
            return 0
      
        current = self.head
        count = 1

        while current:
            current = current.next
            if current is self.head:
                break
            count += 1

        return count
    
l = csLinkedList()
l.append(10)
print(l.count())

m = csLinkedList()
m.append(20)
m.append(30)
m.append(40)
print(m.count())

n = csLinkedList()
print(n.count())
