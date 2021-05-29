
#Resursive Method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def make_list(data):
    head = Node(data[0])
    for element in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(element)
    return head
def print_list(head):
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
    print( ' -> '.join(nodes))

class Linked_list:
    def __init__(self):
        self.head = None

def reverseList(head):
 
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rev = reverseList(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rev
        


if __name__ == "__main__":
    ob1 = Linked_list()
    
    list1 = make_list([1,3,5,7])    
    print("Original Linked List: ")
    print_list(list1)
    
    print("\nReverse Linked List: ")
    list2 = reverseList(list1)
    print_list(list2)
                


