"""
Implement two stacks in an array
Your task is to implement  2 stacks in one array efficiently.

Example 1:
Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()

Output:
3 4 -1
Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 
from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 
from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence -1 .
"""
#LIFO
class Stack:
    def __init__(self,limit=3):
        self.limit = limit 
        self.stack = []
        self.stack2 = []
        self.size = 0 

    def __repr__(self):
        return " ".join(str(i) for i in self.stack)

    def print2(self) -> str:
        return " ".join(str(i) for i in self.stack2)
       

    def isEmpty(self):
        return self.size <= 0

    def isFull(self):
        return self.size == self.limit

    def push(self,data):
        if self.isFull():
            print("stack Overflow")
            return
        else:
            self.stack.append(data)            

    def push2(self,data):
        if self.isFull():
            print("stack Overflow")
            return
        else:
            self.stack2.append(data)
            

    def pop(self):
        if self.isEmpty():
            print("Stack UnderFlow")
        else:
            self.stack.pop()
            
    
    def pop2(self):
        if self.isEmpty():
            print("Stack UnderFlow")
        else:
            self.stack2.pop()
           

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(2)
    myStack.push(3)
    print("PUSH: ", myStack)
    myStack.push2(4)
    print("\nPUSH 2: ",myStack)
    
    myStack.pop()
    print("\nPOP: ",myStack)
    myStack.pop2()
    print("\nPOP 2: ",myStack)
    
        