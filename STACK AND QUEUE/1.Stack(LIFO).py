"""
Stack Data Structure (Introduction and Program)
Difficulty Level : Easy
Last Updated : 10 Mar, 2021
Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

Mainly the following three basic operations are performed in the stack:

Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else false.
                                                    pop()
                                                  /
(deleting and inserting)                 | | | | | -> Push
                                                 \
                                                 Top 
"""
class Stack(object):
    def __init__(self,limit=10):
        self.stack = []
        self.size = 0
        self.limit = limit

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.stack])

    def isEmpty(self):
        return self.size <= 0 

    def isFull(self):
        return self.size == self.limit

    
    def push(self, data):
        if self.isFull():
            print("stack overflow")
            return         # Stack overflow
        else:
            self.stack.append(data)
            self.size += 1
    
    def pop(self):
        if len(self.stack) <= 0:
            print("Stack UnderFlow") # Stack underflow
        else:
            p = self.stack[-1]
            self.stack.pop()
            self.size -= 1
        return p
            
    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            print("Empyt Stack")
            return
        else:
            return self.stack[-1]

    
if __name__ == "__main__":
    #LIFO
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    print("pushed Elements :-", myStack)
    print('Stack Size:',myStack.getSize() ,'\n')
    print("pop",myStack.pop())# remove from last
    print("pop",myStack.pop()) # remove from last

    print("After pop :-", myStack)
    print('Stack Size:',myStack.getSize())
    print("\npeek Top",myStack.peek())
    
        
