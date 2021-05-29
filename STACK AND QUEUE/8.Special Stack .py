"""
Special Stack 

Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.


Example 1:

Input:
Stack: 18 19 29 15 16
Output: 15
Explanation:
The minimum element of the stack is 15.

"""
class Stack:
    def __init__(self,limit= 10):
        self.stack = []
        self.size = 0 
        self.limit = limit
    def __repr__(self) -> str:
        return " ".join([str(i) for i in self.stack])
        
    def push(self, ele):
        # Code here
        self.stack.append(ele)

    def pop(self):
        # Code here
        p = self.stack[-1]
        self.stack.pop()
        return p

    def isFull(self):
        # Code here
        return len(self.stack) == self.limit

    def isEmpty(self):
        #Code here
        return self.stack == []

    def getMin(self):
        # Code here
        return (min(self.stack))

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(18)
    myStack.push(19)
    myStack.push(29)
    myStack.push(15)
    myStack.push(16)
    print("Elements Pushed:",myStack)
    print("minimum: ", myStack.getMin())

    print("pop: ",myStack.pop())
    print("After pop: ",myStack)

    
    
