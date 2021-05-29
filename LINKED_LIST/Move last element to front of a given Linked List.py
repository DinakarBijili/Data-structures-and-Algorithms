"""
Move last element to front of a given Linked List

Write a function that moves the last element to the front in a given Singly Linked List. For example, if the given Linked List is 1->2->3->4->5, then the function should change the list to 5->1->2->3->4.

"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def makelist(data):
    head = Node(data[0])
    for elements in data[1: ]:
        ptr = head
        while ptr.next:
            ptr = ptr.next 
        ptr.next = Node(elements)

    return head


def printList(head):
    nodes = []
    ptr = head

    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr.next is None:
            nodes.append("[Tail %s]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)

        ptr = ptr.next 
    print(" -> ".join(nodes))


class Linked_list:
    def __init__(self) :
        self.head = None

    def move_last_to_first(self, head):
        curr = head
        sec_last = None
        
        while curr and curr.next:
            sec_last = curr 
            curr = curr.next # head moving to next 
        sec_last.next = None # if here second last value reached.that next value is None

        curr.next = head # make head to next 
        head = curr # head to curr
        return head

if __name__ == "__main__":
    obj = Linked_list()
    list1 = makelist([1,2,3,4,5])
    print("Original List: ")
    printList(list1)

    print("\nLast to first element: ")
    printList(obj.move_last_to_first(list1))
