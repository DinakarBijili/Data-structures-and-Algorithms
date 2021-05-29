"""
Middle of the Linked List

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

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

def printList(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr is None:
            nodes.append("[Tail %s]]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)
        ptr = ptr.next
    print(" -> ".join(nodes))

class Linked_list:
        def __init__(self):
            self.head = None

        def Middle_os_linkedList(self, head):
            slow_ptr = head
            fast_ptr = head
    
            if head is not None:
                while (fast_ptr is not None and fast_ptr.next is not None):
                    fast_ptr = fast_ptr.next.next
                    slow_ptr = slow_ptr.next
                # print("The middle element is: ", slow_ptr.data)
                return slow_ptr

if __name__ == "__main__":
    obj = Linked_list()
    list1 = makelist([1,2,3,4,5])
    print("Original Linked List: ")
    printList(list1)


    print("\nMiddle val of LinkedList: ")
    printList(obj.Middle_os_linkedList(list1))

