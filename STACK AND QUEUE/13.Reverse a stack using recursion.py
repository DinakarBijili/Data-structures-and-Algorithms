"""
Reverse a stack using recursion

The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one at the bottom of the stack. 
For example, let the input stack be  

    1  <-- top
    2
    3
    4    
First 4 is inserted at the bottom.
    4 <-- top

Then 3 is inserted at the bottom
    4 <-- top    
    3

Then 2 is inserted at the bottom
    4 <-- top    
    3 
    2
     
Then 1 is inserted at the bottom
    4 <-- top    
    3 
    2
    1

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
    def print_it(self):
        for data in reversed(self.stack):
            print(data)

def insert_bottom(stack, data):
    if stack.isEmpty():
        stack.push(data)
    else:
        deleted_elem = stack.pop()
        insert_bottom(stack, data)
        stack.push(deleted_elem)


def reverse(stack):
    if stack.isEmpty():
       pass
    else:
        popped = stack.pop() # pop all until it stack is empty
        reverse(stack)
        insert_bottom(stack,popped)
    

if __name__ == "__main__":
    #LIFO
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    myStack.push(5)
    print("pushed Elements :-")
    myStack.print_it()
    
    reverse(myStack)
    print("Reversed stack: ")
    myStack.print_it()
    