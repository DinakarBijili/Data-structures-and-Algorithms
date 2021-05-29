"""
Find pairs with given sum in doubly linked list

Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value x, without using any extra space? 

Example:  

Input : head : 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
        x = 7
Output: (6, 1), (5,2)

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

def Count_triple_pairs(head, x = 7):
    ptr1 = head
    ptr2 = None
    count = 0
    while (ptr1 != None):
        ptr2 = ptr1.next
        while (ptr2 != None):
                if ((ptr1.data +ptr2.data ) == x):
                    count += 1
                    print ("Pairs","(",ptr1.data, ptr2.data,")","==", x )
                ptr2 = ptr2.next
        ptr1 = ptr1.next
        
    return count

if __name__== "__main__":
    obj = Linked_list()
    head = makeList([1,2,4,5,6,8,9])
    print("Original Linked List: ")
    PrintList(head)

    print("\nPairs of Linked List of X: ")
    res = (Count_triple_pairs(head))
    print(res,"pairs")




        





    

    