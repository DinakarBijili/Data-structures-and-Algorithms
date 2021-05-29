"""
Check if Linked List is Palindrome

Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

Example 1:

Input:
N = 3
value[] = {1,2,1}
Output: 1
Explanation: The given linked list is
1 2 1 , which is a palindrome and
Hence, the output is 1.
Example 2:

Input:
N = 4
value[] = {1,2,3,4}
Output: 0
Explanation: The given linked list
is 1 2 3 4 , which is not a palindrome
and Hence, the output is 0.

"""
class Node:
    def __init__(self, data ):
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


def PrintList(head):
    nodes = []
    ptr = head
    while ptr:
        if ptr is head:
            nodes.append("[Head %s]"%ptr.data)

        elif ptr is None:
            nodes.append("[Tail %s] -> [None]]"%ptr.data)
        else:
            nodes.append("[%s]"%ptr.data)

        ptr = ptr.next
    print (" -> ".join(nodes))


class Linked_list:
    def __init__(self):
        self.head = None

def Check_Palindrome(list):
    ptr = list
    stack = []
    isplaindrome =  True
    
    while ptr != None:
        stack.append(ptr.data) # Storing Data
         
        ptr = ptr.next  # move 

    while list != None:
        i = stack.pop() # pop data from stack and add to i 
        
        if list.data == i: #if  first and last is equal  stack values store in i  then stack become empty  
            isplaindrome = True
        else:
            isplaindrome = False # else if first and last is not same then the list.data is not equal then stop 
            break
    
        list = list.next
    
    return isplaindrome


if __name__ == "__main__":
    obj = Linked_list()
    list = makeList([5, 1, 1 ,5, 4, 3, 2, 3, 3, 3, 3 ,3, 2, 2, 1, 2, 2, 1, 5, 5, 5, 1, 5, 2, 3, 3, 2, 2, 1, 5, 3, 3, 2, 3, 4, 2, 1, 2, 4, 5])
    
    result = Check_Palindrome(list)
    print(result)
    
