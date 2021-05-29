"""
Sort a stack
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2

"""
from collections import deque 
# Insert the given key into the sorted stack while maintaining its sorted order.
# This is similar to the recursive insertion sort routine
def sortedInsert(stack, key):
    # base case: if the stack is empty or
    # the key is greater than all elements in the stack
    if not stack or key > stack[-1]:
        stack.append(key)
        return
 
    ''' We reach here when the key is smaller than the top element '''
 
    # remove the top element
    top = stack.pop()
 
    # recur for the remaining elements in the stack
    sortedInsert(stack, key)
 
    # insert the popped element back into the stack
    stack.append(top)
 
 
# Recursive method to sort a stack
def sortStack(stack):
    # return stack.sort() -> you can also use directly sort method
    # base case: stack is empty
    if not stack:
        return
    # remove the top element
    top = stack.pop()

    # recur for the remaining elements in the stack
    sortStack(stack)
 
    # insert the popped element back into the sorted stack
    sortedInsert(stack, top)
 
        
    
if __name__ == "__main__":
    myStack = [5, -2, 9, -7, 3]
    stack = deque(myStack)
    print("Pushed Elements: ",myStack)

    sortStack(myStack)

    print("sorted Stack: ", myStack)
    


        

        

