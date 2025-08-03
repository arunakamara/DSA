from linkedlist_class import LinkedList

def remove(self, index):
        if index < 0 or index >= self.length:
            return None
     
        # if node to be removed is the head node
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
     
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
     
            popped_node = temp.next
            
            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp
     
            temp.next = temp.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        

