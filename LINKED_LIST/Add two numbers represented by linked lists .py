# """
# Add two numbers represented by linked lists 

# Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. The sum list is a linked list representation of the addition of two input numbers from the last.

# Example 1:

# Input:
# N = 2
# valueN[] = {4,5}
# M = 3
# valueM[] = {3,4,5}
# Output: 3 9 0  
# Explanation: For the given two linked
# list (4 5) and (3 4 5), after adding
# the two linked list resultant linked
# list will be (3 9 0).
# Example 2:

# Input:
# N = 2
# valueN[] = {6,3}
# M = 1
# valueM[] = {7}
# Output: 7 0
# Explanation: For the given two linked
# list (6 3) and (7), after adding the
# two linked list resultant linked list
# will be (7 0).

# """    
class ListNode:
   def __init__(self, data):
      self.data = data
      self.next = None

def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
def print_list(head):
    nodes =[]
    ptr = head
    while ptr: 
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr is None:
             nodes.append("[Tail %s]"%ptr.data)
        else:
             nodes.append("[%s]"%ptr.data)

        ptr = ptr.next 
    print(" -> ".join(nodes))

# class Solution:
#     def __init__(self):
#         self.head = None

def addTwoNumbers(l1,l2):
    pass



if __name__ == "__main__":
    ob1 = ListNode
    l1 = make_list([0,2,1])
    l2 = make_list([0,3,2])
    print("Original Linked List: ")
    print_list(l1)
    print_list(l2)

    print("\nSum of two linked List: ")
    print(addTwoNumbers(l1, l2))
