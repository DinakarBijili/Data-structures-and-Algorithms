"""
Rotate Doubly linked list by N nodes

Given a doubly linked list, rotate the linked list counter-clockwise by N nodes. Here N is a given positive integer and is smaller than the count of nodes in linked list.


N = 2

Rotated List:


Examples:

Input : a  b  c  d  e   N = 2
Output : c  d  e  a  b 

Input : a  b  c  d  e  f  g  h   N = 4
Output : e  f  g  h  a  b  c  d 

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def set_next(self):
        return self.next

def makeList(data):
    head = Node(data[0])
    for elements in data[1: ]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(elements)

    return head

def PrintList(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr.next is None:
            nodes.append("[Tail %s] ->[None]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)

        ptr = ptr.next

    print(" -> ".join(nodes))


class Linked_list:
    def __init__(self):
        self.head = None

def Rotate_LinkedList_of_N_nodes(head, N = 2):
    if N == 0:
       return 
    # list = a <-> b <-> c <-> d <-> e. 
    curr = head
     
    # current will either point to Nth 
    # or None after this loop. Current 
    # will point to node 'b'
    count = 1
    while count < N and curr != None:
        curr = curr.next
        count += 1

    # If current is None, N is greater 
    # than or equal to count of nodes 
    # in linked list. Don't change the 
    # list in this case 
    if curr == None:
        return
    
    # current points to Nth node. Store 
    # it in a variable. NthNode points to 
    # node 'b' in the above example 
    Nthnode = curr

    # current will point to last node 
    # after this loop current will point 
    # to node 'e'
    while curr.next != None:
        curr = curr.next

    curr.next = head
    

    # Change prev of Head node to current 
    # Prev of 'a' is now changed to node 'e' 
    head.prev = curr

    # head is now changed to node 'c' 
    head = Nthnode.next

    # Change prev of New Head node to None 
    # Because Prev of Head Node in Doubly 
    # linked list is None 
    head.prev = None

    # change next of Nth node to None 
    # next of 'b' is now None 
    Nthnode.next = None
  
    return head

if __name__== "__main__":
    obj = Linked_list()
    head = makeList(['a','b','c','d','e'])
    print("Original Linked List: ")
    PrintList(head)

    print("\nPairs of Linked List of N=2: ")
    PrintList(Rotate_LinkedList_of_N_nodes(head))
    




        