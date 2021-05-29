"""
Given a linked list of 0s, 1s and 2s, sort it.

Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Example 1:

Input:
N = 8
value[] = {1,2,2,1,2,0,2,2}
Output: 0 1 1 2 2 2 2 2
Explanation: All the 0s are segregated
to the left end of the linked list,
2s to the right end of the list, and
1s in between.
Example 2:

Input:
N = 4
value[] = {2,2,0,1}
Output: 0 1 2 2
Explanation: After arranging all the
0s,1s and 2s in the given format,
the output will be 0 1 2 2.

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def makeList(data):
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
            nodes.append("[Tail %s] ->[None]]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)
        ptr = ptr.next
    print(" -> ".join(nodes))

class Linked_list:
    def __init__(self):
        self.head = None

def sort_linked_list_bu_0_1_2(head):
    if head is None or head.next is None:
        return None

    first = Node(0)
    second = Node(0)
    third = Node(0)

    zero = first 
    one = second 
    two = third 

    ptr = head
    while ptr:
        if ptr.data == 0:
            zero.next = ptr
            zero = zero.next
        elif ptr.data == 1:
            one.next = ptr
            one = one.next
        else:
            two.next = ptr
            two = two.next

        ptr = ptr.next

    zero.next = second.next  if second.next else third.next
    one.next = third.next 
    two.next = None

    return first.next
if __name__ == "__main__":
    obj = Linked_list()
    head = makeList([2, 2, 0, 2, 0, 2, 2, 0, 0, 2, 0])
    print("Original Linked List: ")
    printList(head)

    print("\nSorted 0 1 2 SOrted Linked list : ")
    printList(sort_linked_list_bu_0_1_2(head))
