"""
Next Greater Elemen

Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
Example 2:

Input: 
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to 
6 is 8, for 8 there is no larger elements 
hence it is -1, for 0 it is 1 , for 1 it 
is 3 and then for 3 there is no larger 
element on right and hence -1.

"""

# def nextLargerElement(arr):
#         stack = []
    
#         for i in range(len(arr)):
#             next = -1
#             for j in range(i+1, len(arr)):
#                 if arr[i] <= arr[j]:
#                     next = arr[j]
#                     stack.append(arr[j])
#                     break
                
#             print(str(arr[i]) + " --> " + str(next))
        

# if __name__ == "__main__":
#     arr = [1, 3, 2, 4]
#     nextLargerElement(arr)

# USING STACK 
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")

    else:
        return stack.pop()

"""def pairs"""
def printNGE(arr):
    s = createStack()
    element = 0
    next = 0
  
    # push the first element to stack
    push(s, arr[0])
  
    # iterate for rest of the elements
    for i in range(1, len(arr), 1):
        next = arr[i]
  
        if isEmpty(s) == False:
  
            # if stack is not empty, then pop an element from stack
            element = pop(s)
  
            '''If the popped element is smaller than next, then
                a) print the pair
                b) keep popping while elements are smaller and
                   stack is not empty '''
            while element < next:
                print(str(element) + " --> " + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)
  
            '''If element is greater than next, then push
               the element back '''
            if element > next:
                push(s, element)
  
        '''push next to stack so that we can find
           next greater for it '''
        push(s, next)
  
    '''After iterating over the loop, the remaining
       elements in stack do not have the next greater
       element, so print -1 for them '''
  
    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + " --> " + str(next))
  
  
# Driver code
arr = [11, 13, 21, 3]
printNGE(arr) 

 


    

   

