from linkedlist_quest import LinkedList 


def remove_duplicates(ll):
    if ll.head is None:
        return
 
    current_node = ll.head
    prev_node = None
 
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current_node
        current_node = current_node.next
 
    ll.tail = prev_node  
    return ll

def main():

    l = LinkedList()
    l.generate(20, 1, 10)
    print(l)
    remove_duplicates(l)
    print(l)


if __name__ == "__main__":
    main()