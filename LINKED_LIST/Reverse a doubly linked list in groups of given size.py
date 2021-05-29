"""
Reverse a doubly linked list in groups of given size

Input : 10 <-> 8 <-> 4 <-> 2
    k = 2
output : 8 <-> 10 <-> 2 <-> 4

"""
class Node:
    def __init__(self, data ):
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


def PrintList(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)
        elif ptr.next is None:
            nodes.append("[Tail %s] <-> [None]]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)

        ptr = ptr.next 
    print(" <-> ".join(nodes))


class Linked_List:
    def __init__(self):
        self.head = None

    def Reverse_LL_by_size(self,head, K=3):
        temp = Node(0) # 0 head
        temp.next = head
        prev, curr = None, head
        lp, lc = temp , curr
        count = K
        while curr:
            while count > 0 and curr:
                following = curr.next
                curr.next = prev
                
                prev, curr = curr,following

                count -= 1
            lp.next, lc.next = prev, curr
            lp, lc = lc,curr
            count = K
        return temp.next

if __name__ == "__main__":
    obj = Linked_List()
    head = makeList([1,2,3,4,5,6,7,8,9,10])
    print("Doubly Original Linked List: ")
    PrintList(head)

    print("\nReverse Linked List by K: ")
    PrintList(obj.Reverse_LL_by_size(head))
    

        