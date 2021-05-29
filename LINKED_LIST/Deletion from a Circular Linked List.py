"""
Deletion from a Circular Linked List


Input : 2->5->7->8->10->(head node)
        data = 5
Output : 2->7->8->10->(head node)

Input : 2->5->7->8->10->(head node)
         7
Output : 2->5->8->10->2(head node)

"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data = d

def makeList(data):
    head = Node(data[0])
    for elements in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next 

        ptr.next = Node(elements)
    return head


def PrintList(head):
    nodes = []
    if nodes is None:
        return None
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


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0
    def get_size(self):
        return self.size


    def Delete_circular_list(self, head, key= 7):
        # If linked list is empty
        if (head == None):
            return

        # If the list contains only a single node
        if((head).data == key and (head).next == head):
        
            head = None
    
        last = head
        d = None
        
        # If head is to be deleted
        if((head).data == key) :
            
            # Find the last node of the list
            while(last.next != head):
                last = last.next
                
            # Point last node to the next of head i.e.
            # the second node of the list
            last.next = (head).next
            head = last.next
       
        
        # Either the node to be deleted is not found
        # or the end of list is not reached
        while(last.next != head and last.next.get_data() != key) :
            last = last.next
    
        # If node to be deleted was found
        if(last.next.data == key) :
            d = last.next
            last.next = d.next
        
        else:
            print("no such keyfound")
        
        return head
                
            
if __name__ == "__main__":
    obj = Linked_List()
    head = makeList([2,4,5])
    print("Original Linked List:")
    PrintList(head)


    print("\nDeleted value From Linked List: ")
    PrintList(obj.Delete_circular_list(head))
    
    

    
    


    