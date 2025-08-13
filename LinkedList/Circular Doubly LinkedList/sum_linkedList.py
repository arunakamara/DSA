from linkedlist_quest import LinkedList

def sumList(llA, llB):
    """
    Takes two lists with reversed digits format
    Returns a new list that contain the sum of the two list also in reversed digits format
    Time Complexity - O(n)
    Space Complexity - O(n)
    """

    # Initialize n1 to the head of the first list
    n1 = llA.head

    # Initialize n1 to the head of the first list
    n2 = llB.head

    # Initialize carry to 0
    carry = 0

    # Create a new list
    ll = LinkedList()

    # Loop through both the lists
    while n1 or n2:
        result = carry

        # Add the corresponding nodes of the lists
        if n1:
            result += n1.value
            n1 = n1.next

        if n2:
            result += n2.value
            n2 = n2.next
        
        # Append the 1's digit to the new list created
        ll.add(int(result % 10))

        # Assign the 10's digit to carry
        carry = result / 10

    # Return the new list
    return ll

lA = LinkedList()
lA.add(7)
lA.add(1)
lA.add(6)

lB = LinkedList()
lB.add(5)
lB.add(9)
lB.add(2)

print(lA)
print(lB)
print(sumList(lA, lB))
