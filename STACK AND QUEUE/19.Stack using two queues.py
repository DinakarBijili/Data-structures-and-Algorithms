"""
Stack using two queues 

Implement a Stack using two queues q1 and q2.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the 
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4  
Example 2:

Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1

"""
class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.stack])

    def isEmpty(self):
        return self.stack == []
    def push(self,data):
        return self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return -1
        else: 
            p = self.stack[0]
            self.stack.pop(0)
        return p
    

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(2)
    myStack.pop()
    myStack.pop()
    myStack.push(3)
    # myStack.push(3)
    # myStack.pop()
    # myStack.push(4)
    
    # myStack.pop()
    