"""
Reverse a Linked List in groups of given size

Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def makelist(data):
    head = Node(data[0])
    for elements in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(elements)
    return head

def printlist(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head: %s]"%ptr.data)
        elif ptr.next is None:
            nodes.append("[Tail: %s] -> [None]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)
        ptr = ptr.next
    print(" -> ".join(nodes))

class Linked_list:
    def __init__(self):
        self.head = None
    def reverse_of_size(self, head, k=4):
        new_stack = []
        prev = None
        current = head
        while (current != None):
            val = 0

            while (current != None and val < k): # if val is < 4
                new_stack.append(current.data) # adding to new_stack
                current = current.next # current increase to next 
                val+=1  # val also increase by 1 thround next
            
            # Now pop the elements of stack one by one
            while new_stack:

                # If final list has not been started yet.
                if prev is None:
                    prev = Node(new_stack.pop())
                    head = prev

                else:
                    prev.next = Node(new_stack.pop())
                    prev = prev.next
        prev.next = None
        return head

if __name__ == "__main__":
    obj = Linked_list()
    list1 = makelist([1,2,2,4,5,6,7,8])
    
    print("Original Linked_List: ")
    printlist(list1)
        
    print("\n Reverse Linked_List of Size K: ")
    printlist(obj.reverse_of_size(list1))
