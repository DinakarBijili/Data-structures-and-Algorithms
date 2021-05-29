"""
Design a stack with operations on middle element

How to implement a stack which will support following operations in O(1) time complexity? 
1) push() which adds an element to the top of stack. 
2) pop() which removes an element from top of stack. 
3) findMiddle() which will return middle element of the stack. 
4) deleteMiddle() which will delete the middle element. 
Push and pop are standard stack operations. 
The important question is, whether to use a linked list or array for implementation of stack? 
Please note that, we need to find and delete middle element. Deleting an element from middle is not O(1) for array. Also, we may need to move the middle pointer up when we push an element and move down when we pop(). In singly linked list, moving middle pointer in both directions is not possible. 
The idea is to use Doubly Linked List (DLL). We can delete middle element in O(1) time by maintaining mid pointer. We can move mid pointer in both directions using previous and next pointers. 
Following is implementation of push(), pop() and findMiddle() operations. Implementation of deleteMiddle() is left as an exercise. If there are even elements in stack, findMiddle() returns the second middle element. For example, if stack contains {1, 2, 3, 4}, then findMiddle() would return 3. 
 
"""
class Stack(object):
    def __init__(self,limit=7):
        self.limit = limit
        self.stack = []
        self.size = 0

    def __str__(self):
        return " ".join([str(i) for i in self.stack])

    def isEmpty(self):
        return self.size <= 0

    def isFull(self):
        return self.size == self.limit
        
    def push(self, data):
        if self.isFull():
            print("Stack OverFlow")
            return
        else:
            self.stack.append(data)
            self.size += 1

    def pop(self):
        if len(self.stack) <= 0:
            print("Stack is Empty")
            return
        else:
            p = self.stack[-1]
            self.stack.pop()
            self.size -= 1
        return p
        
    def findMiddle(self):
        if self.isEmpty():
            print("Stack is Empty")
            return 
        else:
            for i,j in enumerate(self.stack):
                m = len(self.stack)//2
                if i == m:
                    return j

    def deleteMiddle(self):
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            self.stack.remove(self.findMiddle())
                    

if __name__ == "__main__":
    myStack = Stack()
    #Push
    myStack.push(11)
    myStack.push(22)
    myStack.push(33)
    myStack.push(44)
    myStack.push(55)
    myStack.push(66)
    myStack.push(77)
    print("Pushed elements: ",myStack)
    #pop
    print("\npop:",myStack.pop())
    print("\npop:",myStack.pop())
    print("\nAfter Pop:",myStack)
    
    # middle value
    print("\nMiddle value: ",myStack.findMiddle())

    #deleted middle val
    myStack.deleteMiddle()
    print("\nAfter Deleting Middle",myStack)
    

    

        