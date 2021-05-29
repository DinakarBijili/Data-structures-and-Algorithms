"""
Check If Circular Linked List

Given a singly linked list, find if the linked list is circular or not. A linked list is called circular if it not NULL terminated and all nodes are connected in the form of a cycle. An empty linked list is considered as circular.

Example 1:

Input:
LinkedList: 1->2->3->4->5
(the first and last node is connected,
i.e. 5 --> 1)
Output: 1
Example 2:

Input:
LinkedList: 2->4->6->7->5->1
Output: 0

"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
def makeList(data):
    head = Node(data[0])
    
    for elemensts in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(elemensts)

    return head

def printList(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr.next is None:
            nodes.append("[Tail %s] -> [None]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)

        ptr = ptr.next
    print(" -> ".join(nodes))



class LinkedList:
    def __init__(self):
        self.head= None

    def gethead(self):
        return self.head
        

def Circular(head):
        if head == None:
            return True

        ptr = head.next
        i = 0

        while ((ptr is not None) and (ptr is not head)):
            i += 1
            ptr = ptr.next
        
        return (ptr == head)
         


if __name__ == "__main__":
    obj = LinkedList()
    list = makeList([1,2,3,4])
    print("Original Linked List: ")
    printList(list)

    print("\nCircular Linked List: ")
    result  = Circular(list)
    print(result)
    # if Circular()



