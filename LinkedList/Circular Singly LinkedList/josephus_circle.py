from cs_linkedlist_class import CSLinkedList, Node

class csLinkedList(CSLinkedList):
    def josephus_circle(self, step):
        """
        Returns the last remaining person in the circle
        Time Complexity - O(n^2)
        Space Complexity - O(1)
        """

        current = self.head

        while self.count_nodes() > 1:
            count = 1

            while count !=  step:
                current = current.next
                count += 1

            print(f"Removed: {current.value}")
            self.delete_by_value(current.value)
            current = current.next

        return f"Last person left standing: {current.value}"


l = csLinkedList()
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(60)
print(l.josephus_circle(5))