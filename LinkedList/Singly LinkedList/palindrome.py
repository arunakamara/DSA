from linkedlist_class import LinkedList

class Linked_list(LinkedList):
    def __repr__(self):
        current = self.head

        result = ''

        while current:
            if current is self.tail:
                result += str(current.value)
            else:
                result +=  str(current.value) + ' -> '
            
            current = current.next
        
        return result

def isPalindrome(l_list):
    """
    Return True if the given list is palindrome else False
    """
    # Find the middle of the linkedlist
    slow = fast = l_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    # Reverse the second half of the list
    prev = None

    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Compare the reversed second half with the first half of the original list
    current = l_list.head
    while prev:
        if current.value != prev.value:
            return False
        
        current = current.next
        prev = prev.next

    return True



