from linkedlist_quest import LinkedList, Node

def intersection(llA, llB):
    """
    Checks if two lists are intersecting and returns the intersecting node if they are
    If they are not intersecting returns False
    Time Complexity - O(n)
    Space Complexity - O(1)
    """

    # For two lists to intersect, they must have the same tail
    # Check if the lists have the same tail, if not return False
    if llA.tail is not llB.tail:
        return False
    
    # Identify the longer and shorter list using the len method
    shorter = llA if len(llA) < len(llB) else llB
    longer = llA if len(llA) > len(llB) else llB

    # Find the difference in length between the two list
    diff = len(longer) - len(shorter)

    # Assign a pointer to the head of both lists
    longerNode = longer.head
    shorterNode = shorter.head

    # Move the pointer of the longer list diff-nodes forward
    # This is to get rid of the difference in length of the lists
    # So that while looping through them, we can reach the intersecting node at the same time
    for _ in range(diff):
        longerNode = longerNode.next

    # Move both pointers forward until the both point to the same node
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    # You can now return either of the nodes
    return longerNode 




# Helper addition method
def addSameNode(llA, llB, value):
    """
    An helper function to add a single node to both lists
    Time Complexity - O(1)
    Space Complexity - O(1)
    """
    # Create a temp node with the given value
    tempNode = Node(value)

    # Add temp node to the end of list A
    llA.tail.next = tempNode
    llA.tail = tempNode

    # Add temp node to the end of list B
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(3, 0, 10)

llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(f"Intersected Node: {intersection(llA, llB)}")

