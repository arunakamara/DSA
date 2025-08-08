from cs_linkedlist_class import CSLinkedList, Node

def insert_into_sorted(self, new_node):

    if self.head is None:
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        self.length += 1

    if self.head.value >= new_node.value:
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.length += 1
    
    elif self.tail.value <= new_node.value:
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head
        self.length += 1

    else:
        current = self.head

        while current:
            if current.next.value >= new_node.value:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                return 
            current = current.next
            if current is self.head:
                break


l = CSLinkedList()
l.append(1)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(60)
print(l)
insert_into_sorted(l, Node(5))
print(l)
# print(l.split_list())

