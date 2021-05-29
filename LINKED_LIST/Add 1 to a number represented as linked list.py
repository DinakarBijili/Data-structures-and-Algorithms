"""
Add 1 to a number represented as linked list 
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457 
Example 2:

Input:
LinkedList: 1->2->3
Output: 124 

"""

class Node:
     def __init__(self, data) :
         self.data = data 
         self.next = None

def makeList(data):
    head = Node(data[0])
    for elements in data[1:]:
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
    def __init__(self):
        self.head = None

    def Add1_to_end(self, head):
        pass
            


if __name__ == "__main__":
    obj = Linked_list()
    list1 = makeList([4,5,6])
    print("Original Linked List: ")
    printList(list1)

    print("\nAdd 1 to end: ")
    printList(obj.Add1_to_end(list1))