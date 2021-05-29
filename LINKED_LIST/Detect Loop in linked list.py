class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def makeList(data):
    head = Node(data[0])

    for elements in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next 
        ptr.next = Node(elements)
    return head

def get_node(head, pos):
    if pos != -1:
        p = 0
        ptr = head
        while ptr.next:
            ptr =ptr.next
            p += 1
        return ptr
class Linked_list:
    def __init__(self):
        self.head = None
    
    def Detect_loop(self, head):
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
        return False

if __name__ == "__main__":
    obj = Linked_list()
    head = makeList([5,3,2,0,-4,7])
    pos = 1
    last_node = get_node(head, 5)
    last_node.next = get_node(head, pos)
    print(obj.Detect_loop(head))