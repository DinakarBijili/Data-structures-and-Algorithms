"""
Merge Sort for Linked List 

Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.
Note: If the length of linked list is odd, then the extra node should go in the first list while splitting.

Example 1:

Input:
N = 5
value[]  = {3,5,2,4,1}
Output: 1 2 3 4 5
Explanation: After sorting the given
linked list, the resultant matrix
will be 1->2->3->4->5.
Example 2:

Input:
N = 3
value[]  = {9,15,0}
Output: 0 9 15
Explanation: After sorting the given
linked list , resultant will be
0->9->15.

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


# Takes two lists sorted in increasing order and merge their nodes
# to make one big sorted list, which is returned
def sortedMerge(a, b):
        #base case
        if a is None:
            return b
        if b is None:
            return a

        # pick either a or b and recurse
        if a.data <= b.data:
            result = a
            result.next = sortedMerge(a.next, b)
        else:
            result = b
            result.next = sortedMerge(a, b.next)

        return result


'''
    Split the given list's nodes into front and back halves,
    If the length is odd, the extra node should go in the front list.
    It uses the fast/slow pointer strategy
'''
def split(list):
      # if the length is less than 2, handle it separately
    if list is None or list.next is None:
        return list, None
 
    (left, right) = (list, list.next)
 
    # advance `fast` two nodes, and advance `slow` one node
    while right:
        right = right.next
        if right:
            left = left.next
            right = right.next
 
    # `slow` is before the midpoint of the list, so split it in two
    # at that point.
    ret = (list, left.next)
    left.next = None
 
    return ret
    
# Sort a given linked list using the merge sort algorithm
def mergesort(list):
    # base case — length 0 or 1
    if list is None or list.next is None:
        return list
    # split `list` into `a` and `b` sublists
    left, right = split(list)
 
    # recursively sort the sublists
    left = mergesort(left)
    right = mergesort(right)
 
    # answer = merge the two sorted lists
    return sortedMerge(left, right)
 

        



if __name__ == "__main__":
    obj = LinkedList()
    list = makeList([9,6,8,7,1,4,2,5,3])
    print("Original Linked List: ")
    printList(list)

    print("\nMerge Sorted Linked List: ")
    result  = mergesort(list)
    printList(result)

