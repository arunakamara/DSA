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

    
    def pop_first(self):
        """
        Deletes and return the first node of the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """

        # If the list is empty
        if self.head is None:
            return None
        
        # Assign the head to popped_none as it will be deleted
        popped_node = self.head

        # Assign both head and tail to None if the length is 1
        if self.length == 1:
            self.head = self.tail = None
        
        else:

            # Assign the head pointer to the second node
            self.head = self.head.next

            # Make the tail node now pointes to the new head node
            self.tail.next = self.head

            # To disconnect the deleted node, assign its next value to None
            popped_node.next = None

        # Decrement the length value
        self.length -= 1

        # Return the deleted node
        return popped_node
    
    def pop(self):
        """
        Deletes and return the last node of the list
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # If the list is empty
        if self.head is None:
            return None
        
        # Assign the tail to popped_none as it will be deleted
        popped_node = self.tail

        # Assign both head and tail to None if the length is 1
        if self.length == 1:
            self.head = self.tail = None
        
        else:
            
            current = self.head

            # Loop through till you reach the second-to-last node
            while current.next is not self.tail:
                current = current.next

            # Make the second-to-last node points to the head
            current.next = self.head

            # Assign the second-to-last node to self.tail
            self.tail = current

            # Make the popped node points to None in order to disconnect it from the list
            popped_node.next = None
       
        # Return the deleted node
        self.length -= 1

        # Return the popped node
        return popped_node

                
    def remove(self, index):
        """
        Deletes and returns the node at the given index
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        if index < 0 or index >= self.length:
            return None
        

        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        else:

            # Use the get method to get the node just before the node to be deleted
            prev_node = self.get(index-1)

            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None

            self.length -= 1
            return popped_node
        
    def delete_all(self):
        """
        Delete all the nodes in the list
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if self.head is None:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        # Empty list
        if self.head is None:
            return False
            
        if self.head == self.tail and self.head.value == value:
                self.head = None
                self.tail = None
                self.length = 0
                return True
        
        prev = None
        current = self.head
        
        while True:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                
                self.length -= 1
                return True
            
            prev = current
            current = current.next
            if current == self.head:
                break
        return False

    def split_list(self):
        """
        Splits a list into two equal halves if even 
        If odd the extra goes to the first half
        Time Complexity - O(n)
        Space Complexity - O(n)
        """
        if self.length == 0:
            return None, None
        
        # We added 1 to the length in order to ensure that
        # for odd lengths, the extra one element will be in the first list
        mid = (self.length + 1) // 2

        # Initialize count to 1, to keep track of when the loop reaches the middle of the list
        count = 1

        # Create two lists to hold the first and second half of the original list
        first_list = CSLinkedList()
        second_list = CSLinkedList()

        # Set a pointer to the head of the original list
        current = self.head

        # Initialize a variable to keep track of the last node of the first half
        last_first_list = None

        # Loops through the first half of the original list and append each node to the first list
        while count <= mid:
            first_list.append(current.value)
            last_first_list = current
            current = current.next
            count += 1


        # Set the tail of the first half
        if last_first_list:                         # Checks if there is at least one node in the first list
            first_list.tail = last_first_list       # Sets the tail of first_list to its last node
            first_list.tail.next = first_list.head  # Make the tail points to the head of the first list


        # Handle the second half
        # Loops through the second half of the list and appends each node to the second list
        while current != self.head:
            second_list.append(current.value)
            current = current.next

                
        # Set the tail of the second half
        if second_list.length > 0:                      # Checks if the second list has at least one node
            second_list.tail = self.tail                # Set its tail to the tail of the original list
            second_list.tail.next = second_list.head    # Make the tail points to the head of the second list

        # Return both first and second list
        return first_list, second_list
    
    def is_Sorted(self):
        """
        Return True if sorted, else False
        Time Complexity - O(n)
        Space Complexity - O(1)
        """

        # An empty list is considered to be sorted
        if self.head is None:
            return True
        
        # current = self.head
        # while current.next != self.head:
        #     if current.value > current.next.data:
        #         return False
        #     temp = temp.next

        dummy = Node(float('-inf'))
        prev = dummy
        dummy.next = self.head
        current = self.head

        while current:
            if prev.value > current.value:
                return False
            prev = current
            current = current.next
            if current is self.head:
                break
        
        return True
   

def main():
    csl = CSLinkedList()
    csl.append(10)
    csl.append(20)
    csl.append(30)
    csl.append(40)
    csl.append(50)
    print(csl)

if __name__ == "__main__":
    main()




        
