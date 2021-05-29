"""
Stack Permutations (Check if an array is stack permutation of other)

Examples:

Input : First array: 1, 2, 3  
        Second array: 2, 1, 3
Output : Yes
Procedure:
push 1 from input to stack
push 2 from input to stack
pop 2 from stack to output
pop 1 from stack to output
push 3 from input to stack
pop 3 from stack to output


Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Not Possible  

"""
class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self) -> str:
        return " ".join([str(i) for i in self.stack])


    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        return self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

def Stack_permutation(first,second):
    pass

if __name__ == "__main__":
    myStack = Stack()
    first = [1,2,3]
    second = [2,1,3]
    print(Stack_permutation(first,second))
