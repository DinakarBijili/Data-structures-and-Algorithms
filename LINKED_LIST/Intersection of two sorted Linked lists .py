"""
Intersection of two sorted Linked lists 

Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. The new list should be made with its own memory — the original lists should not be changed.

Example 1:

Input:
L1 = 1->2->3->4->6
L2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given first two
linked list, 2, 4 and 6 are the elements
in the intersection.
Example 2:

Input:
L1 = 10->20->40->50
L2 = 15->40
Output: 40

"""
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

class Solution:
    def __init__(self):
        self.head = None

    def push(self,n):
        new_node = ListNode(n)
        new_node.next = self.head
        self.head = new_node

    def intersect(self,head):
       pass

if __name__ == "__main__":
    obj = Solution()
    l1 = make_list([0,2,1])
    l2 = make_list([0,3,2])
    print("Original Linked List: ")
    print_list(l1)
    print_list(l2)

    print("\nIntersection of two linked List: ")
    print_list(obj.intersect(l1,l2))
    
