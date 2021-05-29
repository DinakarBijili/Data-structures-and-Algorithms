class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

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
        
    def quick_sort(self,head):
        ptr = head
        printList(ptr)
        less = []
        high = []
        mid = (self.size//2) if(self.size % 2 == 0) else((self.size+1)//2)
        pass
        



if __name__ == "__main__":
    obj = LinkedList()
    list = makeList([9,6,8,7,1,4,2,5,3])
    print("Original Linked List: ")
    printList(list)

    print("\nMerge Sorted Linked List: ")
    result  = obj.quick_sort(list)
    # printList(result)

