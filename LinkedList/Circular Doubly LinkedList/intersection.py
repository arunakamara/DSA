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








